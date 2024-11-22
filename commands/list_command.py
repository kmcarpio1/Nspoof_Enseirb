from tabulate import tabulate
from termcolor import colored
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from websites import WEBSITES

def list_command(params): 
    
    data = WEBSITES

    def formatted_item(row):
        return [row[0], "Activé" if row[1] == 1 else "Désactivé", row[2], colored("En cours d'attaque" if row[3] == 1 else "Arrêté", "green" if row[3] == 1 else "red")]

    websites_formatted = map(formatted_item, WEBSITES)

    headers = ["Domaine", "HTTPS", "Identifiants récupérés", "Status"]

    print(tabulate(websites_formatted, headers, tablefmt="grid"))
