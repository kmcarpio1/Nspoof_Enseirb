#!/bin/bash

echo ""

echo -e "------------------------------------------------"
echo -e "        Welcome to NSPOOF conf assistant        "
echo -e "------------------------------------------------"

echo -e "-- Test de la configuration --"

# Check if port 4000 is available
if ! nc -z 127.0.0.1 4000; then
    echo -e "[OUI] Port 4000 non utilisé"
else
    echo -e "[NON] Port 4000 non utilisé"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo -e "[NON] Python installé"
    exit 1
else
    echo -e "[OUI] Python installé"
fi

# Check if PIP is installed
if ! command -v pip3 &> /dev/null
then
    echo -e "[NON] PIP installé"
    exit 1
else
    echo -e "[OUI] PIP installé"
fi

# Check if NGINX is installed
if systemctl is-active --quiet nginx
then
    echo -e "[OUI] Nginx web server installé"
else
    echo -e "[NON] Nginx web server installé"
    echo -e "Installation de Nginx web server ..."
    apt install -y --quiet nginx
fi

# Check if apache is NOT installed
if systemctl is-active --quiet apache2
then
    echo -e "[NON] Apache web server non installé"
    echo -e "Désactivation de Apache web server ..."
    systemctl stop apache2
else
    echo -e "[OUI] Apache web server non installé"
fi

echo -e ""

echo -e "-- Installation d'environnement --"

# If virtual env is founded delete VENV
if [ -d "python3-nspoof" ]; then
    echo -e "[FAIT] Suppression de l'environnement virtuel"
    rm -rf python3-nspoof
fi

# Recreate venv
echo -e "[FAIT] Creation de l'environnement virtuel"
python3 -m venv python3-nspoof

# Activate venv
echo -e "[FAIT] Activation de l'environnement virtuel"
source python3-nspoof/bin/activate

# Installing dependancies
if [ -f "requirements.txt" ]; then
    echo -e "[FAIT] Installation des dépendances de requirements.txt"
    pip install --quiet -r requirements.txt
fi

# Desactivating forwarding on host
sudo sysctl -w net.ipv6.conf.all.forwarding=0 > /dev/null 2>&1
sudo sysctl -w net.ipv6.conf.default.forwarding=0 > /dev/null 2>&1
sudo sysctl -w net.ipv4.ip_forward=0 > /dev/null 2>&1
echo "[FAIT] Désactivation forwarding"

echo -e ""

echo -e "-- Configuration --"

while true; do

    if [ -f "environment.py" ]; then
        rm -rf "environment.py"
    fi

    read -p "Emplacements des manifests NGINX [vide = /etc/nginx/sites-enabled] : " manifests
    read -p "Emplacements des sites web NGINX [vide = /var/www                ] : " websites

    if [ -z "$manifests" ]; then
        manifests="/etc/nginx/sites-enabled"
    fi

    if [ -z "$websites" ]; then
        websites="/var/www"
    fi

    SCRIPT_DIR=$(dirname "$(realpath "$BASH_SOURCE")")

    NGINX_MANIFESTS="$manifests" WEBSERVER_FILES_LOCATION="$websites" NSPOOF_LOCATION="$SCRIPT_DIR" envsubst < environment-template.py > environment.py

    if [ -d "$manifests" ]; then
        break
    else
        echo "$manifests n'existe pas"
    fi

    if [ -d "$websites" ]; then
        break
    else
        echo "$websites n'existe pas"
    fi

done

echo -e "[STATUS] Configuration terminée ! Nspoof est prêt à être utilisé !\n"

echo -e "-----------------------------------------"
echo -e "              Avertissement              "
echo -e "-----------------------------------------\n"

echo -e "Cet outil est destiné uniquement à
être utilisé sur des systèmes et des
infrastructures que vous possédez ou
pour lesquels vous avez une autorisation
explicite de tester. Toute utilisation
non autorisée sur des réseaux ou des
systèmes sans consentement est illégale
et peut entraîner de graves conséquences.
Les développeurs et distributeurs de cet
outil ne cautionnent ni ne soutiennent les
activités illégales.\n"
echo -e "-----------------------------------------\n"

python3 nspoof.py