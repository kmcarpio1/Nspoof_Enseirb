import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES

def ena_site_command(params):

	if len(params) != 1:
		print("Vous devez spécifier un site à activer.")
		return

	try:
		WEBSITES[int(params[0]) - 1][3] = 1
	except IndexError:
		print("Le site n'existe pas.")

	return