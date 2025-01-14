from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

#
# Function returning the real MAC_adress of a machine from it IP_adress.
#
def get_MAC(dst_IP):
    if dst_IP not in ARPTABLE:
        return False
    return ARPTABLE[dst_IP]

# def get_MAC_with_ARP(dst_IP):
#     pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=dst_IP)
#     rsp = srp(pkt, timeout=1, verbose=False)[0]
#     if rsp: #if response received
#         return rsp[0][1].hwsrc #return the MAC adress
#     else:
#         return False #else false
