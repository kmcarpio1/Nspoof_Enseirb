import sys
import os
import shutil
import signal
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from corethreads.coremanager import manager

def exit_command(params):

    if not manager.startEvent.is_set():
        print("Attaque non démarrée")
        sys.exit()
        return

    manager.stopEvent.set();

    if manager.thread1.is_alive():
        manager.thread1.join();
    print("[ARRETE] Man-In-The-Middle ARP")


    print('2')
    if manager.thread2.is_alive():
        manager.thread2.join();
    print("[ARRETE] Sniffeur DNS")

    print('3')
    if manager.thread3.is_alive():
        manager.thread3.join();
    print("[ARRETE] Sniffeur autres paquets")

    print('4')
    subprocess.run(['rm', '-rf', ENV['webserver_location'] + "/nspoof*"], check=True);
    subprocess.run(['rm', '-rf', ENV['nginx_manifests'] + "/nspoof*"], check=True);
    subprocess.run(['rm', '-rf', ENV['nspoof_location'] + "/credentials/*"], check=True);
    subprocess.run(['rm', '-rf', ENV['nspoof_location'] + "/tmp"], check=True);

    print("[OK] Suppression des fichiers")
    print("[OK] Arrêt du programme")

    if ATTACK_STATUS['wspid'] != 0:
        os.kill(ATTACK_STATUS['wspid'], signal.SIGTERM)

    sys.exit()