import os
import shutil
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

def renew_config_file(domains, idd, https):

    dst = ENV['nginx_manifests']

    copied = os.path.join(dst, 'nspoof' + str(idd) + ".conf")

    if os.path.exists(copied):
        os.remove(copied)
    
    if https == 1:
        shutil.copy(ENV['nspoof_location'] + '/nginx_templates/nginx.https.conf', copied)
    else:
        shutil.copy(ENV['nspoof_location'] + '/nginx_templates/nginx.http.conf', copied)

    with open(copied, 'r') as file:
        content = file.read()

    content = content.replace("{{DOMAINS}}", ", ".join(map(str, domains)))
    content = content.replace("{{WEBSITE_ID}}", str(idd))

    with open(copied, 'w') as file:
        file.write(content)

    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)
    return