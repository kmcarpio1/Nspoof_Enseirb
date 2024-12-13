from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from mac_management import *

def forwarder(pkt):
    if pkt[IP] and pkt[Ether]:
        self_mac = get_if_hwaddr(str(ATTACK_STATUS['iface']))
        pkt[Ether].src = pkt[Ether].dst #we replace the sender MAC with our
        dst_MAC = get_MAC(pkt[IP].src) #we replace the destination MAC by the real one 

        if dst_MAC:
            pkt[Ether].dst = dst_MAC
            sendp(pkt)
            if IP in pkt:
                print("Forwarding package from" + str(pkt[IP].src) + " to " + str(pkt[IP].dst) + " for domain name "+ str(pkt[DNS][DNSQR].qname.decode('utf-8')) + " On a request " + str(pkt.getlayer(DNS).qd.qtype))
            else :
                print("Forwarding package")
        else:
            print(f"Error: Unable to resolve MAC address for {dst_ip}")
