from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS

def dns_sorting_start():
    websites = WEBSITES
    dns= ATTACK_STATUS['dns']
	victims = ATTACK_STATUS['victims']
    network = ipadress.ip_network(victims, strict=False)
    

def dns_sniffer(iface):
    iface = str(ATTACK_STATUS['iface'])
    

    sniff(filter="udp port 53", prn= lambda pkt : dns_sorting_start(pkt), iface=iface) #udp port 53 for DNS requests #pkt is the received packet by sniff