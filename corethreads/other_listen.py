from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from forwarder import *

#
# Function launching the forwarding function in another thread.
#
def launch_forward(pkt, self_mac):
    if(pkt[Ether].dst == self_mac):
        thread = threading.Thread(target=forwarder, args=(pkt,))
        thread.start()

#
# Function starting sniffing all the request in the network that are not DNS requests/responses.
#
def other_sniffer(stopEvent):

    def stop_sniffer(pkt):
        return stopEvent.is_set()

    iface = str(ATTACK_STATUS['iface'])
    self_mac = get_if_hwaddr(iface)
    print("[STARTED] Other packets sniffer")
    sniff(filter="(udp or tcp) and not port 53", prn=lambda pkt: launch_forward(pkt, self_mac), iface=iface, stop_filter=stop_sniffer)