import sys
import os
import tarfile
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from delete_config_file import delete_config_file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *


#
# Handler to remove a website from the spoofed websites.
#
def rem_site_command(params):

    # Check if an attack is already in progress
    if ATTACK_STATUS['status'] != 0:
        print("The attack is already in progress.")
        return

    # Ensure that exactly one parameter (site to remove) is specified
    if len(params) != 1:
        print("You must specify a site to remove.")
        return

    try:
        # Get the site ID from the provided parameter (adjusted for 0-based index)
        idd = WEBSITES[int(params[0]) - 1][0]
        # Remove the site from the WEBSITES list
        WEBSITES.remove(WEBSITES[int(params[0]) - 1])
    except IndexError:
        # Handle the case where the site does not exist
        print("The site does not exist.")

    # Deletion of the folder and nginx manifest associated with the site
    try:

        # Construct paths for the website directory and manifest
        dir_to_delete = ENV['webserver_location'] + '/website' + str(idd)
        manifest_to_delete = ENV['nginx_manifests'] + '/website' + str(idd) + ".conf"

        # Remove the website directory if it exists
        if os.path.exists(dir_to_delete):
            shutil.rmtree(dir_to_delete)

    except:
        # Handle any errors during folder and manifest deletion
        print("Error occurred while deleting the folder and manifest.")
        return

    return
