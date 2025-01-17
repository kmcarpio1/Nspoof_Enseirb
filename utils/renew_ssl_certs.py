import os
import shutil
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509.oid import NameOID
from cryptography import x509
import datetime

# Function for generating private key
def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

# Function to renew the generation of a certificate for a domain
def renew_ssl_certs(domain):

    # Get certificate location folder
    dst = ENV['certificates_location']

    # If nspoof folder doesnt exists inside this directory then create it
    if not os.path.exists(dst + "/nspoof"):
        os.mkdir(dst + "/nspoof")

    # Check if there is an existing CA
    if not os.path.exists(ENV['nspoof_location'] + "/nspoof_ca_cert.pem") or not os.path.exists(ENV['nspoof_location'] + "/nspoof_private_key.pem"):
        print("You must generate an authority before. Type gen_ca.")
        return

    # If CA exists then get it and its private key

    with open(ENV['nspoof_location'] + "/nspoof_private_key.pem", "rb") as f:
        ca_private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
        )

    with open(ENV['nspoof_location'] + "/nspoof_ca_cert.pem", "rb") as f:
        ca_cert = x509.load_pem_x509_certificate(f.read())

    # If there is already an existing certificate then remove it
    if os.path.exists(dst + "/nspoof/" + domain):
        shutil.rmtree(dst + "/nspoof/" + domain)

    # Recreate the folder
    os.mkdir(dst + "/nspoof/" + domain)

    private_key = generate_private_key()

    # Create the subject
    subject = x509.Name([x509.NameAttribute(NameOID.COUNTRY_NAME, "FR"),x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Aquitaine"),x509.NameAttribute(NameOID.LOCALITY_NAME, "Bordeaux"),x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Nspoof"),x509.NameAttribute(NameOID.COMMON_NAME, domain),])

    # Generate a new cert
    cert = x509.CertificateBuilder().subject_name(subject).issuer_name(ca_cert.subject).public_key(private_key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(datetime.datetime.utcnow()).not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365)).add_extension(x509.SubjectAlternativeName([x509.DNSName(domain)]),critical=False,).sign(ca_private_key, hashes.SHA256())

    # Paste private key in a new file
    with open(dst + "/nspoof/" + domain + "/private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
    ))

    # And finally past certificate on a new file
    with open(dst + "/nspoof/" + domain + "/public.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print("Certificat signé créé et sauvegardé.")

    # Return 1 (will be checked BEFORE creating nginx configuration file)
    return 1