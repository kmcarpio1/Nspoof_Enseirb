import sys
import os
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fx')))
from attack_status import ATTACK_STATUS
from websites import WEBSITES
from renew_config_file import renew_config_file
from env import ENV

def exit_command(params):

    folders = [ENV['webserver_location'], ENV['nginx_manifests']]

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
    print("[OK] Arrêt du programme")
    sys.exit()