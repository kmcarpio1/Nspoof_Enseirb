import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

#
# Handler to temporary enable a website.
#
def ena_site_command(params):

	# Check if attack status is pending or not
	if ATTACK_STATUS['status'] != 0:
		print("L'attaque est déja en cours.")
		return

	if len(params) != 1:
		print("Vous devez spécifier un site à activer.")
		return

	try:
		WEBSITES[int(params[0]) - 1][3] = 1
	except IndexError:
		print("Le site n'existe pas.")

	return