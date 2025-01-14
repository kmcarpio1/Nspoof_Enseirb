from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from mac_management import *

#
# Function forwarding any package, changing the mac adress of the package. It replace the automatic forwarding that should bu disable when this program is running.
#
def forwarder(pkt):
    if pkt[IP] and pkt[Ether]:
        self_mac = get_if_hwaddr(str(ATTACK_STATUS['iface']))
        pkt[Ether].src = pkt[Ether].dst #we replace the sender MAC with our

        if ipaddress.ip_address(pkt[IP].src) in ipaddress.ip_network(ATTACK_STATUS['victims'], strict=False) or pkt[IP].src == ATTACK_STATUS["dns"]:
            dst_MAC = get_MAC(pkt[IP].src) #we replace the destination MAC by the real one 
        else:
            dst_MAC = get_MAC(ATTACK_STATUS["dns"])

        if dst_MAC:
            pkt[Ether].dst = dst_MAC
            try:
                sendp(pkt, verbose=False)
            except Exception as e:
                pass
        #    print("Forwarding package from" + str(pkt[IP].src) + " to " + str(pkt[IP].dst) )
        #else:
        #    print(f"Error: Unable to resolve MAC address for {str(pkt[IP].src)}")
