#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed."
    exit 1
fi

# Check if PIP is installed
if ! command -v pip3 &> /dev/null
then
    echo "Error: pip is not installed."
    exit 1
fi

# Check if NGINX is installed
if systemctl is-active --quiet nginx
then
    echo "Get nginx configuration ..."
else
    apt install -y nginx
fi

# Check if apache is NOT installed
if systemctl is-active --quiet apache2
then
    systemctl stop apache2
fi

# Check if iptables is installed
if ! command -v iptables &> /dev/null
then
    apt install -y iptables
fi
echo "Restore IPV4 special rules"
iptables-restore < iptables_templates/rules.v4

# If virtual env is founded delete VENV
if [ -d "python3-nspoof" ]; then
    rm -rf python3-nspoof
    exit
fi

# Recreate venv
echo "Creating virtual environment..."
python3 -m venv python3-nspoof

# Activate venv
echo "Activating virtual environment..."
source python3-nspoof/bin/activate

# Installing dependancies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

echo "Setup complete. nspoof environment is ready"

python3 nspoof.py