import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

def dis_site_command(params):

	if len(params) != 1:
		print("Vous devez spécifier un site à désactiver.")
		return

	try:
		WEBSITES[int(params[0]) - 1][3] = 0
	except IndexError:
		print("Le site n'existe pas.")

	return