import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *

def backup():
    # Répertoires spécifiques
    history_dir = os.path.join(ENV["nspoof_location"], "history")
    credentials_dir = os.path.join(ENV["nspoof_location"], "credentials")
    backup_dir = os.path.join(ENV["nspoof_location"], "backup")

    # Crée le répertoire de sauvegarde s'il n'existe pas
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Génère un nom de fichier unique avec un timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"session_{timestamp}.backup")

    # Récupère tous les fichiers .txt directement dans history et credentials
    all_files = []
    for directory in [history_dir, credentials_dir]:
        print(directory)
        if os.path.exists(directory):
            all_files.extend(
                os.path.join(directory, file) for file in os.listdir(directory)
            )

    # Écrit les contenus des fichiers dans le fichier de sauvegarde
    with open(backup_file, "w", encoding="utf-8") as backup:
        for file in all_files:
            backup.write(f"===== File : {file} =====\n")
            with open(file, "r", encoding="utf-8") as f:
                backup.write(f.read())
            backup.write("\n====================================\n\n")
