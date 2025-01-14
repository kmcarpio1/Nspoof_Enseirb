import threading

ARPTABLE = {}

ATTACK_STATUS = {
	"status": 0,
	"dns": "172.21.0.254",
	"victims": "172.21.201.117",
	'iface': "eth1",
	'wspid': 0
}

ENV = {
	"nginx_manifests": "/etc/nginx/sites-enabled",
	"webserver_location": "/var/www",
	"nspoof_location": "/home/paul/Documents/nspoof",
	"tmp_location": "/home/paul/Documents/nspoof/tmp",
}

WEBSITES = []

stop_event = threading.Event()