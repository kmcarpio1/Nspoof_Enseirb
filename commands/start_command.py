import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
from attack_status import ATTACK_STATUS
import threading
from corethreads.arp import arp

def start_command(params):

	if ATTACK_STATUS['status'] == 0:

		t = threading.Thread(target=arp)
		print("Démarrage de l'attaque")
		ATTACK_STATUS['status'] = 1
		t.start()

	else:

		print("Attaque déja démarrée");
