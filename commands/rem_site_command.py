import sys
import os
import tarfile
import shutil
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
		idd = WEBSITES[int(params[0]) - 1][0]
		WEBSITES.remove(WEBSITES[int(params[0]) - 1])
	except IndexError:
		print("Le site n'existe pas.")

	# Deletion of folder
	try:

		dir_to_delete = '/var/www/nspoof/website' + str(idd)

		if os.path.exists(dir_to_delete):
			shutil.rmtree(dir_to_delete)

	except:
		print("Erreur lors de la supression du dossier.")
		return

	return