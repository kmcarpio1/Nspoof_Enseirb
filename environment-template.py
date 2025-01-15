import threading

ARPTABLE = {}

ATTACK_STATUS = {
	"status": 0,
	"dns": "${DNS_SERVER}",
	"victims": "${VICTIMS}",
	'iface': "${IFACE}",
	'wspid': 0
}

ENV = {
	"nginx_manifests": "${NGINX_MANIFESTS}",
	"webserver_location": "${WEBSERVER_FILES_LOCATION}",
	"nspoof_location": "${NSPOOF_LOCATION}",
	"certificates_location": "${CERTIFICATES_LOCATION}"
}

WEBSITES = []

stop_event = threading.Event()