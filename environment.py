import threading

ARPTABLE = {}

ATTACK_STATUS = {
	"status": 0,
	"dns": "192.168.63.254",
	"victims": "192.168.49.83/32",
	'iface': "wlp0s20f3",
	'wspid': 0
}

ENV = {
	"nginx_manifests": "/etc/nginx/sites-enabled",
	"webserver_location": "/var/www",
	"nspoof_location": "/home/kenzo/nspoof",
	"certificates_location": "/etc/ssl/certs"
}

WEBSITES = []

stop_event = threading.Event()