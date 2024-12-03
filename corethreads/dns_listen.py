from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS

def dns_sorting_start(pkt):
    websites = WEBSITES
    dns= ATTACK_STATUS['dns']
	victims = ATTACK_STATUS['victims']
    network = ipadress.ip_network(victims, strict=False)

    ip_src = pkt[IP].src 
    ip_dst = pkt[IP].dst

    if pkt.haslayer(DNS): #check if there is a DNS layer
        dns_layer = pkt[DNS]
        dns_check(websites, dns, network, pkt, ip_src, ip_dst)
    #comportement sinon ?????

def dns_check(websites, dns, network, pkt, ip_src, ip_dst):
    if dns_layer.qr == 1 AND ip_src == dns AND ip_dst in network AND check_website() : #if it's a response we want to block the one from the dns server to the victim
        if dns_layer.an : #check if there is a response
            domain_name = pkt[DNS].an.rrname.decode('utf-8')
            website = check_website(website, domain_name)
            if website: #if there is a corresponding website in out data
                if ip_dst not in website[4]: #if we didn't already colelcted the information for this IP on this website
                    create_dns_response(website, dns, network, pkt, ip_src, ip_dst)
                    return

    elif dns_layer.qr == 0 AND ip_src in network AND ip_dst == dns : #if it's a request we want to block the one from the victim to the dns server
        domain_name = pkt[DNS][DNSQR].qname.decode('utf-8')
        website = check_website(website, domain_name)
        if website: #if there is a corresponding website in out data
            if ip_src not in website[4]: #if we didn't already colelcted the information for this IP on this website
                create_dns_after_response(website, dns, network, pkt, ip_src, ip_dst)        
                return
 
    forward_dns(pkt) #if something is wrong, it will forward the package

def check_website(websites,domain_name):
    for website in websites:
        if domain_name in website[1]:
            return website
    return False

def forward_dns(pkt):
    #jsute refaire le meme paquet en changeant les mac (on forward, les ip restent les même, juste la mac de l'envoyeur doit etre remplacée par la notre,et notre mac par celle du receveur)

def create_dns_response(website, dns, network, pkt, ip_src, ip_dst):
    #créer un nouveau de réponse à partir des infos du paquet de request pkt reçu, en mettant comme ip celle de notre site malvaillant    

def create_dns_after_response(website, dns, network, pkt, ip_src, ip_dst):
    #euuuuuuuh en vrai jsp, on bloque juste nan ? 

def dns_sniffer(iface):
    iface = str(ATTACK_STATUS['iface'])
    

    sniff(filter="udp port 53", prn= lambda pkt : dns_sorting_start(pkt), iface=iface) #udp port 53 for DNS requests #pkt is the received packet by sniff