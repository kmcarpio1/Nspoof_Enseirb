import os
import shutil
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from env import ENV

def delete_config_file(idd):

    dst = ENV['nginx_manifests']

    os.makedirs(dst, exist_ok=True)
    copied = os.path.join(dst, 'website' + str(idd) + ".conf")

    if os.path.exists(copied):
        os.remove(copied)

    return