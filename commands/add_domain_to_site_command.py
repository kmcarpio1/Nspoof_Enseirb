import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES

def add_domain_to_site_command(params):

	if len(params) < 2:
		print("Vous devez spécifier au moins un domaine et un identifiant de site")
		return

	domains = params[:-1]

	try:
		WEBSITES[int(params[-1]) - 1][1].extend(domains)
	except IndexError:
		print("Le site n'existe pas.")

	return