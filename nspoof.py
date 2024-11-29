import sys
import pyfiglet
from commands.fallback_command import fallback_command
from commands.status_command import status_command
from commands.list_command import list_command
from commands.help_command import help_command
from commands.exit_command import exit_command
from commands.start_command import start_command
from commands.show_creds_command import show_creds_command
from commands.set_dns_command import set_dns_command
from commands.set_victims_command import set_victims_command
from commands.set_iface_command import set_iface_command
from commands.add_site_command import add_site_command
from commands.rem_site_command import rem_site_command
from commands.dis_site_command import dis_site_command
from commands.ena_site_command import ena_site_command
from corethreads.arp import arp

COMMANDS = {}

def register_commands():
    COMMANDS['status'] = status_command
    COMMANDS['list'] = list_command
    COMMANDS['help'] = help_command
    COMMANDS['exit'] = exit_command
    COMMANDS['start'] = start_command
    COMMANDS['stop'] = exit_command
    COMMANDS['set_dns'] = set_dns_command
    COMMANDS['set_victims'] = set_victims_command
    COMMANDS['set_iface'] = set_iface_command
    COMMANDS['show_creds'] = show_creds_command
    COMMANDS['add_site'] = add_site_command
    COMMANDS['rem_site'] = rem_site_command
    COMMANDS['dis_site'] = dis_site_command
    COMMANDS['ena_site'] = ena_site_command

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

if __name__ == "__main__":
    ascii_art = pyfiglet.figlet_format("Nspoof")
    print(ascii_art)
    print("RSR Project - (c) BARBARIN Paul - MORENO CARPIO Kenzo")
    interactive_shell()
    thread = threading.Thread(target=arp)
