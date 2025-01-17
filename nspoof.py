import sys
import pyfiglet
import os
import signal
import threading
import readline  # Ajout de readline pour l'autocomplétion
from commands.fallback_command import fallback_command
from commands.status_command import status_command
from commands.list_command import list_command
from commands.help_command import help_command
from commands.exit_command import exit_command
from commands.start_command import start_command
from commands.show_creds_command import show_creds_command
from commands.show_history_command import show_history_command
from commands.add_site_command import add_site_command
from commands.rem_site_command import rem_site_command
from commands.zip_command import zip_command
from commands.gen_ca_command import gen_ca_command
from commands.add_domain_to_site_command import add_domain_to_site_command
from commands.rem_domain_to_site_command import rem_domain_to_site_command
from environment import ENV

COMMANDS = {}

def register_commands():
    COMMANDS['status'] = status_command
    COMMANDS['list'] = list_command
    COMMANDS['help'] = help_command
    COMMANDS['exit'] = exit_command
    COMMANDS['start'] = start_command
    COMMANDS['show_creds'] = show_creds_command
    COMMANDS['show_history'] = show_history_command
    COMMANDS['add_site'] = add_site_command
    COMMANDS['rem_site'] = rem_site_command
    COMMANDS['dis_site'] = dis_site_command
    COMMANDS['ena_site'] = ena_site_command
    COMMANDS['add_domain_to_site'] = add_domain_to_site_command
    COMMANDS['zip'] = zip_command
    COMMANDS['gen_ca'] = gen_ca_command
    COMMANDS['rem_domain_to_site'] = rem_domain_to_site_command
    COMMANDS['exit'] = exit_command


def completion(text, state):
    options = [cmd for cmd in COMMANDS.keys() if cmd.startswith(text)]
    return options[state] if state < len(options) else None

def enable_autocompletion():
    readline.set_completer(completion)
    readline.parse_and_bind("tab: complete")

def exitc(a,b):
    exit_command([])
    return

signal.signal(signal.SIGINT, exitc)
signal.signal(signal.SIGTERM, exitc)

def interactive_shell():
    while True:
        try:
            user_input = input("nspoof >>> ").strip()
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0]
            params = parts[1:]

            if command in COMMANDS:
                COMMANDS[command](params)
            else:
                fallback_command(command)

        except Exception as e:
            print(f"Erreur: {e}")

register_commands()
enable_autocompletion()

if __name__ == "__main__":
    ascii_art = pyfiglet.figlet_format("Nspoof")
    print(ascii_art)
    print("RSR Project - (c) BARBARIN Paul - MORENO CARPIO Kenzo")

    interactive_shell()
