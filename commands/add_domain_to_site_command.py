import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from renew_config_file import renew_config_file

#
# Handler for adding a site to the list of spoofed websites
def add_domain_to_site_command(params):

	# Manage errors on parameters
	if len(params) < 2:
		print("Vous devez spécifier au moins un domaine et un identifiant de site")
		return

	# Get the domain list
	domains = params[:-1]

	# Try to access the domains
	try:
		WEBSITES[int(params[-1]) - 1][1].extend(domains)
	except IndexError:
		print("Le site n'existe pas.")

	renew_config_file(WEBSITES[int(params[-1]) - 1][1], WEBSITES[int(params[-1]) - 1][0], WEBSITES[int(params[-1]) - 1][6])

	return