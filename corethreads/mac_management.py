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
