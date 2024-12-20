import os
import shutil
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

def delete_config_file(idd):

    dst = ENV['nginx_manifests']

    os.makedirs(dst, exist_ok=True)
    copied = os.path.join(dst, 'nspoof' + str(idd) + ".conf")

    if os.path.exists(copied):
        os.remove(copied)

    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)
    return