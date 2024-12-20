import sys
import os
from scapy.all import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
import ipaddress
import threading

lock = threading.Lock()

#
# Launch a request to get ARP address of an IP
#
def arprequest(ip):

    with lock:
        if ip in ARPTABLE:
            return

    arp_resolver_package_victim = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
    mac_victim = srp(arp_resolver_package_victim, timeout=3, verbose=False)

    if mac_victim[0] and mac_victim[0][0] and mac_victim[0][0][1] and mac_victim[0][0][1].hwsrc:
        with lock:
            ARPTABLE[ip] = str(mac_victim[0][0][1].hwsrc)
    return


#
# Thread launched to update ARP table
# 
def arptable():

    # Print a message
    print("[DEMARRE] Scanneur ARP")

    # Parse subnet of victims
    victims = ipaddress.IPv4Network(ATTACK_STATUS['victims'], strict=False);

    # Create a list of threads
    threads = []

    # Iterate on each victim
    for victim in victims.hosts():

        thread = threading.Thread(target=arprequest, args=(str(victim),))
        thread.start()
        threads.append(thread)

    thread = threading.Thread(target=arprequest, args=(str(ATTACK_STATUS['dns']),))
    thread.start()
    threads.append(thread)

    for thread in threads:
        thread.join()

    print("[TERMINE] Scanneur ARP")

    return