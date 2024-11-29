import os
import shutil
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'environment')))
from env import ENV

def renew_config_file(domains, idd, https):

    dst = ENV['nginx_manifests']

    os.makedirs(dst, exist_ok=True)  # Créer le répertoire si nécessaire
    copied = os.path.join(dst, 'website' + str(idd) + ".conf")

    if os.path.exists(copied):
        os.remove(copied)
    
    # Copier le fichier template
    if https == 1:
        shutil.copy(ENV['nspoof_location'] + '/templates/nginx.https.conf', copied)
    else:
        shutil.copy(ENV['nspoof_location'] + '/templates/nginx.http.conf', copied)

    with open(copied, 'r') as file:
        content = file.read()

    content = content.replace("{{DOMAINS}}", ", ".join(map(str, domains)))
    content = content.replace("{{WEBSITE_ID}}", str(idd))

    with open(copied, 'w') as file:
        file.write(content)

    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)
    return