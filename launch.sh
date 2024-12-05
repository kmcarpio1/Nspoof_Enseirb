#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed."
    exit 1
fi

if ! command -v pip3 &> /dev/null
then
    echo "Error: pip is not installed."
    exit 1
fi

if systemctl is-active --quiet nginx
then
    echo "Get nginx configuration ..."
else
    echo "Error: nginx is not installed or is not running."
    exit 1
fi

if systemctl is-active --quiet apache2
then
    echo "Error: apache must be disabled during the usage of nspoof."
    exit 1
fi

mkdir /var/www/nspoof
mkdir /etc/nginx/sites-enabled

if [ -d "python3-nspoof" ]; then
    python3 nspoof.py
    exit
fi

echo "Creating virtual environment..."
python3 -m venv python3-nspoof

echo "Activating virtual environment..."
source python3-nspoof/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

echo "Setup complete. nspoof environment is ready"

python3 nspoof.py