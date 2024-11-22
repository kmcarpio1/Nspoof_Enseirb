import sys
from commands.fallback_command import fallback_command
from commands.status_command import status_command
from commands.help_command import help_command

COMMANDS = {}

def register_commands():
    COMMANDS['status'] = status_command
    COMMANDS['help'] = help_command

def interactive_shell():
    while True:
        try:

            user_input = input(">>> ").strip()
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
    interactive_shell()
