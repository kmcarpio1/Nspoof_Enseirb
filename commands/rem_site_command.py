import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES

def rem_site_command(params):

	if ATTACK_STATUS['status'] != 0:
		print("L'attaque est déja en cours.")
		return

	if len(params) != 1:
		print("Vous devez spécifier un site à supprimer.")
		return

	try:
		WEBSITES.remove(WEBSITES[int(params[0]) - 1])
	except IndexError:
		print("Le site n'existe pas.")

	return