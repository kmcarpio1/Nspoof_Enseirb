from tabulate import tabulate

def help_command(params):

    data = [
        ["help", "Affiche les commandes disponibles"],
        ["status", "Affiche le status de l'attaque en cours"],
        ["list", "Affiche la liste des sites usurpés"],
        ["add_site [domain(s)] [archive]", "Ajouter un site internet à usurper"],
        ["rem_site [domain(s)] [archive]", "Supprimer un site internet à usurper"],
        ["dis_site [site_id]", "Désactiver temporairement un site"],
        ["ena_site [site_id]", "Réactiver un site"],
        ["add_domain_to_site [site_id] [domain(s)]", "Ajouter un domaine à un site à usurper"],
        ["rem_domain_to_site [site_id] [domain(s)]", "Supprimer un domaine à un site à usurper"],
        ["start", "Démarrer l'attaque"],
        ["stop", "Stopper"],
        ["exit", "Terminer l'attaque et le programme"],
    ]

    headers = ["Commande", "Usage"]

    print(tabulate(data, headers, tablefmt="grid"))