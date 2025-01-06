import sys
import os
import tarfile
import shutil
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

#
# Handler for clearing history and credentials
#
def clear_all_command(params):

	nspoof_location = ENV['nspoof_location']
	subprocess.call("(sudo rm -rf " + os.path.join(nspoof_location, 'history/*') + ")", shell=True)
	subprocess.call("(sudo rm -rf " + os.path.join(nspoof_location, 'credentials/*') + ")", shell=True)

	return