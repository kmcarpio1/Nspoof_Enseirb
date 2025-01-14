import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from renew_config_file import renew_config_file


#
# Handler to remove a domain for a spoofed website.
#
def rem_domain_to_site_command(params):
    # Ensure at least a domain and a site ID are provided
    if len(params) < 2:
        print("Vous devez spécifier au moins un domaine et un identifiant de site")
        return

    # Extract domains to be removed (all parameters except the last one)
    domains = params[:-1]

    try:
        # Loop through each domain to remove it from the specified site
        for i in range(len(domains)):
            WEBSITES[int(params[-1]) - 1][1].remove(domains[i])  # Adjusting for 0-based index
    except IndexError:
        # Handle the case where the specified site ID doesn't exist
        print("Le site n'existe pas.")
        return

    # Update the configuration file for the modified site
        renew_config_file(WEBSITES[int(params[-1]) - 1][1], WEBSITES[int(params[-1]) - 1][0], WEBSITES[int(params[-1]) - 1][6])
    return
