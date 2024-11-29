import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES

def add_site_command(params):

	if ATTACK_STATUS['status'] != 0:
		print("L'attaque est déja en cours.")
		return

	if len(params) < 2:
		print("Vous devez spécifier au moins un domaine et un le chemin d'un fichier ZIP contenant les fichiers du site à usurper.")
		return

	if len(WEBSITES) == 0:
		idd = 1
	else:
		idd = WEBSITES[-1][0] + 1

	domains = params[:-1]

	new_site = [idd, domains, 0, 1, []]

	WEBSITES.append(new_site)