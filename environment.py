import threading

ARPTABLE = {}

ATTACK_STATUS = {
	"status": 0,
	"dns": "192.168.0.254",
	"victims": "192.168.0.0/24",
	'iface': "eth0",
	'wspid': 0
}

ENV = {
	"nginx_manifests": "/etc/nginx/sites-enabled",
	"webserver_location": "/var/www",
	"nspoof_location": "/home/paul/Documents/nspoof",
	"certificates_location": "/etc/ssl/certs"
}

WEBSITES = []

stop_event = threading.Event()