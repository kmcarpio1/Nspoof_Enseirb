import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

#
# Function to create a backup when the program is exited
#
def backup():

    # Get backup folders
    history_dir = os.path.join(ENV["nspoof_location"], "history")
    credentials_dir = os.path.join(ENV["nspoof_location"], "credentials")
    backup_dir = os.path.join(ENV["nspoof_location"], "backup")

    # Create backup directory if it does'nt exists
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Generate an uniq backup filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"session_{timestamp}.backup")

    # Get all files
    all_files = []
    for directory in [history_dir, credentials_dir]:
        if os.path.exists(directory):
            all_files.extend(
                os.path.join(directory, file) for file in os.listdir(directory)
            )

    # Write backup content
    with open(backup_file, "w", encoding="utf-8") as backup:
        for file in all_files:
            backup.write(f"===== File : {file} =====\n")
            with open(file, "r", encoding="utf-8") as f:
                backup.write(f.read())
            backup.write("\n====================================\n\n")
