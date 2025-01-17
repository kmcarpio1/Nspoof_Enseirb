#!/bin/bash

echo ""

echo -e "------------------------------------------------------------------------------------------------"
echo -e "                                Welcome to NSPOOF conf assistant                                "
echo -e "------------------------------------------------------------------------------------------------"

echo -e "-- Configuration test --"

# Check if port 4000 is available
if ! nc -z 127.0.0.1 4000; then
    echo -e "[PASSED] Port 4000 not used"
else
    echo -e "[ERROR] Port 4000 not used"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo -e "[ERROR] Python installed"
    exit 1
else
    echo -e "[PASSED] Python installed"
fi

# Check if PIP is installed
if ! command -v pip3 &> /dev/null
then
    echo -e "[ERROR] PIP installed"
    exit 1
else
    echo -e "[PASSED] PIP installed"
fi

# Check if apache is NOT installed
if systemctl is-active --quiet apache2
then
    echo -e "[ERROR] Apache web server is not installed"
    echo -e "Desactivation of Apache web server ..."
    systemctl stop apache2
else
    echo -e "[PASSED] Apache web server not installed"
fi

# Check if NGINX is installed
if systemctl is-active --quiet nginx
then
    echo -e "[PASSED] Nginx web server installed"
else
    echo -e "[ERROR] Nginx web server installed"
    echo -e "Installation of Nginx web server ..."
    apt install -y --quiet nginx
fi

echo -e ""

echo -e "-- Environment installation --"

# If virtual env is founded delete VENV
if [ -d "python3-nspoof" ]; then
    echo -e "[DONE] Deletion of virtual environment"
    rm -rf python3-nspoof
fi

# Recreate venv
echo -e "[DONE] Creation of virtual environment"
python3 -m venv python3-nspoof

# Activate venv
echo -e "[DONE] Activation of virtual environment"
source python3-nspoof/bin/activate

# Installing dependancies
if [ -f "requirements.txt" ]; then
    echo -e "[DONE] Installation of dependancies of requirements.txt"
    pip install --quiet -r requirements.txt
fi

# Desactivating forwarding on host
sudo sysctl -w net.ipv6.conf.all.forwarding=0 > /dev/null 2>&1
sudo sysctl -w net.ipv6.conf.default.forwarding=0 > /dev/null 2>&1
sudo sysctl -w net.ipv4.ip_forward=0 > /dev/null 2>&1
echo "[DONE] Forwarding desactivation"
echo "[ALERT] PLEASE CHECK THAT FORWARD HAS BEEN DISACTIVATED -- SOMETIMES PROGRAM CAN'T DO THIS AUTOMATICALLY"
echo "Will pause 3 seconds ..."

echo -e ""

echo -e "-- Configuration --"
echo -e "-- Next time, precise --skip flag if you want to keep default values and skip configuration --"

while true; do

    if [ -f "environment.py" ]; then
        rm -rf "environment.py"
    fi

    skip=false

    for arg in "$@"; do
        if [ "$arg" == "--skip" ]; then
            skip=true
            break
        fi
    done

    if ! $skip; then
        read -p "NGINX manifests location         [vide = /etc/nginx/sites-enabled] : " manifests
        read -p "NGINX websites location          [vide = /var/www                ] : " websites
        read -p "Certificates location            [vide = /etc/ssl/certs          ] : " ssl
        read -p "DNS Servers location             [vide= 192.168.0.254            ] : " dns_server
        read -p "Victims IP/Subnet                [vide= 192.168.0.0/24           ] : " victims
        read -p "Interface                        [vide= eth0                     ] : " iface
    fi

    if [ -z "$manifests" ]; then
        manifests="/etc/nginx/sites-enabled"
    fi

    if [ -z "$websites" ]; then
        websites="/var/www"
    fi

    if [ -z "$ssl" ]; then
        ssl="/etc/ssl/certs"
    fi

    if [ -z "$dns_server" ]; then
        dns_server="192.168.0.254"
    fi

    if [ -z "$victims" ]; then
        victims="192.168.0.0/24"
    fi

    if [ -z "$iface" ]; then
        iface="eth0"
    fi

    SCRIPT_DIR=$(dirname "$(realpath "$BASH_SOURCE")")

    NGINX_MANIFESTS="$manifests" WEBSERVER_FILES_LOCATION="$websites" NSPOOF_LOCATION="$SCRIPT_DIR" CERTIFICATES_LOCATION="$ssl" DNS_SERVER="$dns_server" VICTIMS="$victims" IFACE="$iface" envsubst < environment-template.py > environment.py

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

echo -e "[STATUS] Configuration done !\n"

echo -e "------------------------------------------------------------------------------------------------"
echo -e "                                           Warning                                              "
echo -e "------------------------------------------------------------------------------------------------\n"

echo -e "This tool is intended to be used only on systems and infrastructures that you own or have explicit 
authorization to test. Any unauthorized use on networks or systems without consent is illegal and may 
result in severe consequences. The developers and distributors of this tool do not endorse or support 
illegal activities."
echo -e "------------------------------------------------------------------------------------------------\n"


python3 nspoof.py
