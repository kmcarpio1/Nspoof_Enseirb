import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored


#
# Handler to display the internet history of all victims.
#
def show_history_command(params): 

    # If no parameters are provided, prompt the user to specify an IP address
    if len(params) == 0:

        print("Specify an IP:")

        # Get the path to the history folder
        folder_path = os.path.join(ENV['nspoof_location'], "history")
        # List all files in the history folder
        files = os.listdir(folder_path)
        dt = []
        # Iterate through files and exclude ".gitkeep"
        for file in files:
            if file != ".gitkeep":
                dt.append([file])

        # Display the available history sheets
        headers = ["Available history sheets:"]
        print(tabulate(dt, headers, tablefmt="grid"))

        return

    # Ensure that exactly one parameter (IP address) is provided
    if len(params) != 1:
        print("Usage error. Type help.")
        return

    # Convert the parameter to an IP address
    ip = str(params[0])

    # Construct the file path for the specified IP address
    file_path = ENV['nspoof_location'] + "/history/" + ip

    # Check if the history file exists for the given IP
    if not os.path.exists(file_path):
        print("No history sheet for " + ip)
        return
    
    data = []

    # Open and read the history file for the given IP
    with open(file_path, 'r') as file_:
        for line in file_:
            line = line.strip()
            # Split the line by '|||' if present
            if '|||' in line:
                date, site = line.split('|||')
                # Append the formatted date and site to the data list
                data.append([colored(date, "cyan"), colored(site, 'green')])

    # Define table headers for the history display
    headers = [colored("Date and time", "red"), colored("Visited website", 'red')]

    # Display the history for the specified IP address
    print("History of " + colored(ip, "cyan"))
    print(tabulate(data, headers, tablefmt="grid"))
