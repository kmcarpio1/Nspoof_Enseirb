import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
from attack_status import ATTACK_STATUS
import threading
import subprocess
from corethreads.arp import arp

def start_command(params):

	if ATTACK_STATUS['status'] == 0 and ATTACK_STATUS['wspid'] == 0:

		ATTACK_STATUS['status'] = 1

		thread = threading.Thread(target=arp)
		thread.start()

		process = subprocess.Popen(["python3", "corethreads/credentials_catcher.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		ATTACK_STATUS['wspid'] = process.pid

		print("Démarrage de l'attaque")


	else:

		print("Attaque déja démarrée");
