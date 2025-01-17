from tabulate import tabulate


#
# Handler to display the helps and instructions for all commands.
#
def help_command(params):

    # Build an array with messages
    data = [
        ["help", "Displays the available commands"],
        ["status", "Shows the configuration status"],
        ["list", "Displays the list of spoofed sites"],
        ["add_site domain1 [other_domains] archive https", "Adds a website to spoof"],
        ["rem_site site_id", "Removes a website from spoofing"],
        ["dis_site site_id", "Temporarily disables a site"],
        ["ena_site site_id", "Re-enables a site"],
        ["add_domain_to_site domain1 [other_domains] site_id", "Adds a domain to a site to spoof"],
        ["rem_domain_to_site domain1 [other_domains] site_id", "Removes a domain from a site to spoof"],
        ["zip absolute_path_to_file name_wanted", "Archives a folder as .tar.gz"],
        ["gen_ca", "Generates a certification authority to create certificates"],
        ["show_history", "Shows a history of visited domains"],
        ["show_creds", "Displays captured credentials"],
        ["start", "Starts the attack"],
        ["exit", "Ends the attack and the program. Cleans up files"]
    ]

    headers = ["Commande", "Usage"]

    print(tabulate(data, headers, tablefmt="grid"))