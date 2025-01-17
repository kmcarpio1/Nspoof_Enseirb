import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509.oid import NameOID
from cryptography import x509
import datetime

# Function to generate private key for ca
def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

#
# Handler for generation of CA
#
def gen_ca_command(params):

	# Location on filesystem
	CA_PRIVATE_KEY_FILE = ENV['nspoof_location'] + "/nspoof_private_key.pem"
	CA_CERT_FILE = ENV['nspoof_location'] + "/nspoof_ca_cert.pem"

	# If CA already exists just ask to replace it
	if os.path.exists(CA_CERT_FILE):
		print(f"Certification '{CA_CERT_FILE}' already exists.")
		choice = input("Would you like to replace it ? Warning ! It will cancel all already imported CA on clients (replace/NO) : ").strip().lower()

		if choice == 'replace':
			try:
				os.remove(CA_PRIVATE_KEY_FILE)
				os.remove(CA_CERT_FILE)
				print(f"Certification '{CA_CERT_FILE}' deleted.")
				print(f"Key '{CA_PRIVATE_KEY_FILE}' deleted.")
			except Exception as e:
				print(f"Error on deletion : {e}")
		else:
			print("Aborted.")
			return

	# Generate a random private key
	private_key = generate_private_key()

	# Create a subject for CA
	subject = issuer = x509.Name([x509.NameAttribute(NameOID.COUNTRY_NAME, "FR"),x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Aquitaine"),x509.NameAttribute(NameOID.LOCALITY_NAME, "Bordeaux"),x509.NameAttribute(NameOID.ORGANIZATION_NAME, "NSpoof"),x509.NameAttribute(NameOID.COMMON_NAME, "NSpoof ROOT"),])

	# Build the certificate of CA
	cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(private_key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(datetime.datetime.utcnow()).not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=3650)).add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True,).sign(private_key, hashes.SHA256())

	# Open target file and paste generated private key
	with open(CA_PRIVATE_KEY_FILE, "wb") as f:
		f.write(private_key.private_bytes(
			encoding=serialization.Encoding.PEM,
			format=serialization.PrivateFormat.TraditionalOpenSSL,
			encryption_algorithm=serialization.NoEncryption(),
		))
	
	# Open target file and paste generated CERT
	with open(CA_CERT_FILE, "wb") as f:
		f.write(cert.public_bytes(serialization.Encoding.PEM))

	print("Created CA and saved.")
	return