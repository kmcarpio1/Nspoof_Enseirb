import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from tabulate import tabulate
from termcolor import colored

def show_creds_command(params): 

    if len(params) != 1:
        print("Erreur d'usage. Tapez help pour de l'aide.")
        return

    index = int(params[0]) - 1

    if 0 <= index < len(WEBSITES):

        print("Identifiants récupérés depuis le domaine " + colored(WEBSITES[index][1], "cyan"))

    else:
        print("Erreur. Le site n'existe pas.")
        return