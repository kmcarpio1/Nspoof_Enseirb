import sys
import os
import shutil
import signal
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from corethreads.coremanager import manager

def erase_files():

    nspoof_location = ENV['nspoof_location']
    webserver_location = ENV['webserver_location']
    nginx_manifests = ENV['nginx_manifests']

    subprocess.call("(sudo rm -rf " + os.path.join(nginx_manifests, 'nspoof*') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(webserver_location, 'nspoof*') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(nspoof_location, 'tmp') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(nspoof_location, 'environment.py') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(nginx_manifests, 'nspoof*') + ")", shell=True)
    subprocess.call("(sudo rm -rf " + os.path.join(webserver_location, 'nspoof*') + ")", shell=True)

    return

def exit_command(params):

    if not manager.startEvent.is_set():
        print("Attaque non démarrée")
        erase_files()
        sys.exit()
        return

    manager.stopEvent.set();

    if manager.thread1.is_alive():
        manager.thread1.join();
    print("[ARRETE] Man-In-The-Middle ARP")

    if manager.thread2.is_alive():
        manager.thread2.join();
    print("[ARRETE] Sniffeur DNS")

    if manager.thread3.is_alive():
        manager.thread3.join();
    print("[ARRETE] Sniffeur autres paquets")

    erase_files()

    print("[OK] Suppression des fichiers")
    print("[OK] Arrêt du programme")

    if ATTACK_STATUS['wspid'] != 0:
        os.kill(ATTACK_STATUS['wspid'], signal.SIGTERM)

    sys.exit()