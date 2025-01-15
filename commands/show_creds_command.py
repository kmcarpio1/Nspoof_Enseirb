import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored
from commands.list_command import list_command


#
# Handler to display the credentials collected.
#
def show_creds_command(params):

    # If no parameters are provided, prompt the user to specify a website ID
    if len(params) == 0:
        print("Specify website id:")
        list_command([])  # Call list_command to show available websites
        return

    # Ensure that exactly one parameter is passed (website ID)
    if len(params) != 1:
        print("Usage error. Type help.")
        return

    # Convert the provided website ID to an index (adjusting for 0-based index)
    index = int(params[0]) - 1

    # Check if the index is within valid range
    if 0 <= index < len(WEBSITES):

        # Display the credentials for the specified website
        print("Caught credentials from domain(s) " + colored(WEBSITES[index][1], "cyan"))

        # Construct the file path where the credentials are stored
        file_path = os.path.join(ENV['nspoof_location'] + "/credentials", f"{str(index+1)}")

        # Open and read the credentials file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Display the content of the credentials file
            print(content)

    else:
        # Handle the case where the website does not exist
        print("Error. Website does not exist")
        return
