import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS

def set_victims_command(params):

	if len(params) != 1:
		print("Erreur d'usage. Tapez help pour de l'aide")
		return

	ATTACK_STATUS['victims'] = params[0]