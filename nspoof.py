import sys
import pyfiglet
from commands.fallback_command import fallback_command
from commands.status_command import status_command
from commands.list_command import list_command
from commands.help_command import help_command
from commands.exit_command import exit_command
from commands.start_command import start_command
from commands.stop_command import stop_command

COMMANDS = {}

def register_commands():
    COMMANDS['status'] = status_command
    COMMANDS['list'] = list_command
    COMMANDS['help'] = help_command
    COMMANDS['exit'] = exit_command
    COMMANDS['start'] = start_command
    COMMANDS['stop'] = stop_command

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
                result = COMMANDS[command](params)
                print(result)
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
