                               __ 
                              / _|
  _ __  ___ _ __   ___   ___ | |_ 
 | '_ \/ __| '_ \ / _ \ / _ \|  _|
 | | | \__ \ |_) | (_) | (_) | |  
 |_| |_|___/ .__/ \___/ \___/|_|  
           | |                    
           |_|          


# Nspoof.sh util
## A tool to automate attacks by DNS usurpation
(c) Paul BARBARIN - MORENO CARPIO Kenzo
---
Educative only !

## Launch program
To launch the program, you just have to execute the following command :
```sudo ./launch.sh```

Make sure you have nginx webserver installed on your machine, and NOT APACHE. You must also have Python3 and PIP on your machine.


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
