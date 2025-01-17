import os
import shutil
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

#
# Delete the nginx conf file for a specified idd
#
def delete_config_file(idd):

    # Get NGINX manifests directory
    dst = ENV['nginx_manifests']

    # Create directory if it does'nt exists
    os.makedirs(dst, exist_ok=True)

    # Delete config file if it exists
    
    copied = os.path.join(dst, 'nspoof' + str(idd) + ".conf")

    if os.path.exists(copied):
        os.remove(copied)

    # Restart nginx
    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)
    return