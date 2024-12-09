import sys
import os
import shutil
import signal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from renew_config_file import renew_config_file

def exit_command(params):

    folders = [ENV['webserver_location'], ENV['nginx_manifests'], ENV['nspoof_location'] + "/credentials"]

    for folder in folders:
        if os.path.exists(folder):
            for item in os.listdir(folder):
                item_path = os.path.join(folder, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            os.makedirs(folder, exist_ok=True)

    print("[OK] Suppression des fichiers")

    os.kill(ATTACK_STATUS['wspid'], signal.SIGTERM)

    print("[OK] Arrêt du programme")

    sys.exit()