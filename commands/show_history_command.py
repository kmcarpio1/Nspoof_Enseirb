import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored

#
# Show history
#
def show_history_command(params): 

    if len(params) == 0:

        print("Specify an IP :")

        folder_path = os.path.join(ENV['nspoof_location'], "history")
        files = os.listdir(folder_path)
        dt = []
        for file in files:
            if file != ".gitkeep":
                dt.append([file])

        headers = ["Available history sheets :"]
        print(tabulate(dt, headers, tablefmt="grid"))

        return

    if len(params) != 1:
        print("Usage error. Type help.")
        return

    ip = str(params[0])

    file_path = ENV['nspoof_location'] + "/history/" + ip

    # Vérifiez si le fichier existe
    if not os.path.exists(file_path):
        print("No history sheet for " + ip);
        return
    
    data = []

    with open(file_path, 'r') as file_:
        # Parcours de chaque ligne
        for line in file_:
            line = line.strip()
            if '|||' in line:
                date, site = line.split('|||')
                data.append([colored(date, "cyan"), colored(site, 'green')])

    headers = [colored("Date and time", "red"), colored("Visited website", 'red')]

    print("History of " + colored(ip, "cyan"))
    print(tabulate(data, headers, tablefmt="grid"))