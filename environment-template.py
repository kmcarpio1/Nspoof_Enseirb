import threading

ARPTABLE = {}

ATTACK_STATUS = {
	"status": 0,
	"dns": "172.21.0.254",
	"victims": "172.21.202.39/32",
	'iface': "eth1",
	'wspid': 0
}

ENV = {
	"nginx_manifests": "${NGINX_MANIFESTS}",
	"webserver_location": "${WEBSERVER_FILES_LOCATION}",
	"nspoof_location": "${NSPOOF_LOCATION}",
	"tmp_location": "${NSPOOF_LOCATION}/tmp",
}

WEBSITES = []

stop_event = threading.Event()