import requests
import re

# URL de base, sans le paramètre 'pid'
base_url = "https://rule34.xxx/index.php?page=favorites&s=view&id=1448372&pid="

# En-têtes HTTP, incluant les informations nécessaires pour la requête
headers = {
    "Host": "rule34.xxx",
    "Cookie": "cf_clearance=WKNadjG133imOu_a0VMFOq7RNfHXohcntT1BZbablbQ-1761002511-1.2.1.1-ZXcbuFnZEmlTwBhu6JEzlmfbIlGzJjLzjqFlRiFDDHSvhyMwDH0.LmLHCdNDsNxzeMRhT.c0kZ7Ir_DoYKJxfK._EGvQrJY3ZsqW7Fmn0m0eUZTPJT9JAKjwtEudigpj.6MbGAe7zyOCK7puDmqCawSmquVMeNAMXAH9ljEa1kgK3knbtXM7Meg5lTIVpc3WSxn4.NcJuYZneIu3AZejYJWU9UaG_qR_uTuuepHiK1w; gdpr=1; gdpr-consent=1; user_id=5487729; pass_hash=3697e3b5ef16a46ea6acb10b3900e64337f8d60a",
    "Sec-Ch-Ua": '"Not?A_Brand";v="99", "Chromium";v="130"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://rule34.xxx/index.php?page=favorites&s=view&id=1448372&pid=15250",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
}

# Fonction pour extraire les numéros des posts
def extract_post_numbers(html_content):
    post_numbers = re.findall(r'posts\[(\d+)\]', html_content)
    return post_numbers

# Liste pour stocker tous les numéros extraits
all_post_numbers = []

# Ouverture du fichier en mode écriture (création du fichier s'il n'existe pas)
with open('post_numbers.txt', 'w') as file:
    # Parcours des pages de 15200 à 0, par tranche de 50
    for pid in range(15200, -1, -50):
        url = f"{base_url}{pid}"
        print(f"Récupération de l'URL : {url}")

        # Faire la requête GET pour chaque page
        response = requests.get(url, headers=headers)

        # Vérifier la réponse
        if response.status_code == 200:
            print(f"Page {pid} récupérée avec succès !")
            html_content = response.text
            
            # Extraire les numéros de posts
            post_numbers = extract_post_numbers(html_content)
            all_post_numbers.extend(post_numbers)  # Ajouter les numéros extraits à la liste globale
            
            # Écrire les numéros extraits dans le fichier
            for number in post_numbers:
                file.write(f"{number}\n")  # Un numéro par ligne dans le fichier
        else:
            print(f"Erreur lors de la requête pour la page {pid} : {response.status_code}")

# Afficher tous les numéros extraits
print("Tous les numéros extraits ont été enregistrés dans 'post_numbers.txt'.")
