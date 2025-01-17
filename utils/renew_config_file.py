import os
import shutil
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

#
# Update the nginx configuration file with specified info for specified idd
#
def renew_config_file(domains, idd, https):

    # Get NGINX manifests directory
    dst = ENV['nginx_manifests']

    # Delete config file if it exists

    copied = os.path.join(dst, 'nspoof' + str(idd) + ".conf")

    if os.path.exists(copied):
        os.remove(copied)
    
    # Template file depending on HTTPS activated or not
    if https == 1:
        shutil.copy(ENV['nspoof_location'] + '/nginx_templates/nginx.https.conf', copied)
    else:
        shutil.copy(ENV['nspoof_location'] + '/nginx_templates/nginx.http.conf', copied)

    # Update 
    with open(copied, 'r') as file:
        content = file.read()

    content = content.replace("{{DOMAINS}}", ", ".join(map(str, domains)))
    content = content.replace("{{WEBSITE_ID}}", str(idd))

    content = content.replace("{{CERTIFICATE}}", ENV["certificates_location"] + "/nspoof/" + str(domains[0]) + "/public.pem")
    content = content.replace("{{KEY}}", ENV["certificates_location"] + "/nspoof/" + str(domains[0]) + "/private.pem")

    with open(copied, 'w') as file:
        file.write(content)

    # Restart nginx
    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)
    return