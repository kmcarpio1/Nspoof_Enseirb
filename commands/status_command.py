import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored

def status_command(params): 

    data = [
        [colored("En cours", "green") if ATTACK_STATUS['status'] == 1 else colored("Arrêtée", "red"), ATTACK_STATUS['dns'], ATTACK_STATUS['victims'], ATTACK_STATUS['iface']]
    ]

    headers = ["Status de l'attaque", "Serveurs DNS à usurper", "IP / Subnet victime", "Interface réseau"]

    print(tabulate(data, headers, tablefmt="grid"))