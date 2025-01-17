import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from renew_config_file import renew_config_file

#
# Handler for adding a domain(s) to a website.
#
def add_domain_to_site_command(params):

	# Check if attack status is pending or not
	if ATTACK_STATUS['status'] != 0:
		print("L'attaque est déja en cours.")
		return

	# Manage errors on parameters
	if len(params) < 2:
		print("You must specify a domain and a website identifier.")
		return

	# Get the domain list
	domains = params[:-1]

	# Try to update the domain list of the targeted website
	try:
		WEBSITES[int(params[-1]) - 1][1].extend(domains)
	except IndexError:
		print("The website does not exist")

	# Renew nginx configuration
	renew_config_file(WEBSITES[int(params[-1]) - 1][1], WEBSITES[int(params[-1]) - 1][0], WEBSITES[int(params[-1]) - 1][6])

	return