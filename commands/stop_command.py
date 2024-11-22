import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS

def stop_command(params):
	ATTACK_STATUS['status'] = 0
	print("Attaque stoppée !")