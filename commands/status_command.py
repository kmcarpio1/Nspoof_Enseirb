import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored

#
# Handler to display the configuration and their status.
#
def status_command(params): 

    # Prepare the data to display the attack status
    # If the attack is in progress (status == 1), show "In progress" in green; otherwise, show "Stopped" in red
    data = [
        [colored("In progress", "green") if ATTACK_STATUS['status'] == 1 else colored("Stopped", "red"), 
         ATTACK_STATUS['dns'], 
         ATTACK_STATUS['victims'], 
         ATTACK_STATUS['iface']]
    ]

    # Define the headers for the status table
    headers = ["Attack Status", "DNS Servers to Spoof", "Victim IP / Subnet", "Network Interface"]

    # Print the status table with formatted headers and data
    print(tabulate(data, headers, tablefmt="grid"))
