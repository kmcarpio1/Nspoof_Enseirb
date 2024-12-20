import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored

def show_history_command(params): 

    if len(params) != 1:
        print("Erreur d'usage. Tapez help pour de l'aide")
        return

    ip = str(params[0])

    file_path = ENV['nspoof_location'] + "/history/" + ip

    # Vérifiez si le fichier existe
    if not os.path.exists(file_path):
        print("Aucune entrée d'historique pour " + ip);
        return
    
    data = []

    with open(file_path, 'r') as file_:
        # Parcours de chaque ligne
        for line in file_:
            line = line.strip()
            if '|||' in line:
                date, site = line.split('|||')
                data.append([colored(date, "cyan"), colored(site, 'green')])

    headers = [colored("Date et Heure", "red"), colored("Site visité", 'red')]

    print("Historique de navgation récupéré pour " + colored(ip, "cyan"))
    print(tabulate(data, headers, tablefmt="grid"))