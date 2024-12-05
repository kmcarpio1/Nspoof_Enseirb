import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES
from renew_config_file import renew_config_file

def rem_domain_to_site_command(params):

	if len(params) < 2:
		print("Vous devez spécifier au moins un domaine et un identifiant de site")
		return

	domains = params[:-1]

	try:
		for i in range(len(domains)):
			WEBSITES[int(params[-1]) - 1][1].remove(domains[i])
	except IndexError:
		print("Le site n'existe pas.")

	renew_config_file(WEBSITES[int(params[-1]) - 1][1], WEBSITES[int(params[-1]) - 1][0], WEBSITES[int(params[-1]) - 1][6])

	return