import sys
import os
import shutil
import signal
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from corethreads.coremanager import manager

#
# Function to erase and clean all temporary files.
#
def erase_files():

    nspoof_location = ENV['nspoof_location']
    webserver_location = ENV['webserver_location']
    nginx_manifests = ENV['nginx_manifests']

    subprocess.call("(sudo rm -rf " + os.path.join(nginx_manifests, 'nspoof*') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(webserver_location, 'nspoof*') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(nspoof_location, 'tmp') + ")", shell=True)
    #subprocess.call("(sudo rm -rf " + os.path.join(nspoof_location, 'environment.py') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(nginx_manifests, 'nspoof*') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(webserver_location, 'nspoof*') + ")", shell=True)

    return

#
# Handler to exit and clean the code.
#
def exit_command(params):
    # Check if the attack has not been started
    if not manager.startEvent.is_set():
        print("Attaque non démarrée")
        erase_files()  # Clean up any temporary files
        sys.exit()  # Terminate the program immediately
        return

    # Signal to stop the attack
    manager.stopEvent.set();

    # Wait for thread1 (ARP Man-In-The-Middle) to stop if it's running
    if manager.thread1.is_alive():
        manager.thread1.join();
    print("[ARRETE] Man-In-The-Middle ARP")

    # Wait for thread2 (DNS sniffer) to stop if it's running
    if manager.thread2.is_alive():
        manager.thread2.join();
    print("[ARRETE] Sniffeur DNS")

    # Wait for thread3 (Other packet sniffer) to stop if it's running
    if manager.thread3.is_alive():
        manager.thread3.join();
    print("[ARRETE] Sniffeur autres paquets")

    erase_files()  # Remove temporary files created during the attack

    # Provide feedback on cleanup and termination
    print("[OK] Suppression des fichiers")
    print("[OK] Arrêt du programme")

    # Kill a specific process related to the attack if it exists
    if ATTACK_STATUS['wspid'] != 0:
        os.kill(ATTACK_STATUS['wspid'], signal.SIGTERM)

    sys.exit()  # Terminate the program
