# Nspoof.sh util
tool to automate attacks by DNS usurpation - (c) Paul BARBARIN - MORENO CARPIO Kenzo - RSR Project
---
Educative usage only -- Other usages could be illegal

## Launch program

## Update environment/env.py :

```python
ENV = {
	"nginx_manifests": "/etc/nginx/sites-enabled", # The location of your enabled nginx websites
	"webserver_location": "/var/www/nspoof", # The location of your websites (can be changed)
	"nspoof_location": "/home/paul/Documents/enseirb-nspoof", # The location of nspoof (have to be changed)
	"tmp_location": "/home/paul/Documents/enseirb-nspoof/tmp" # The location of nspoof tmp folder (have to be changed)
}
```
Warning ! All of these folders have to be created BEFORE launching the program.

## Save your current firewall rules
Make sure you don't have installed firewall other than iptables. Please also consider saving your current iptables rules, because it will be lost when the program starts.

## Launch !
To launch the program, you just have to execute the following command :
```sudo ./launch.sh```

---
Pense bete : 

 - Récupérer la liste de domaines que l'on souhaite usurper (dans un coeur a part) et gérer le moteur qui envoie les réponses DNS lorsque les requêtes sont destinées à ces domaines précisément.
 - Ouvrir le serveur web permettant la récupération des identifiants
 - Gérer l'ajout des sites
 
 .zip
 --- index.php
 --- login.php (GENERE PAR NOUS)
 --- domain_name.txt | nom du domaine vers quoi rediriger
 ___ ip.txt | IP:PORT a laquelle on veut envoyer les infos (GENERE PAR NOUS)
