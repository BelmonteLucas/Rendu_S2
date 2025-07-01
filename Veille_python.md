# Veille technologique : Utilisation de Python dans le métier d’administrateur réseau

---

## Introduction

En tant qu'apprenti administrateur réseau, j'ai trouvé intéressant de me pencher sur l'utilisation de Python dans ce métier. Python s'est imposé comme le langage de référence grâce à sa simplicité, ses nombreuses bibliothèques spécialisées et son adaptabilité. C'est un outil précieux pour gérer, surveiller et sécuriser les infrastructures réseau modernes.

---

## 1. Automatisation des tâches réseau

Automatiser les tâches répétitives permet aux administrateurs de gagner du temps, d'améliorer la fiabilité et de réduire les erreurs humaines. Python propose plusieurs bibliothèques adaptées à ces besoins :

- **Paramiko** : permet d'établir des connexions SSH avec des équipements réseau. Idéal pour automatiser l’exécution de commandes à distance, comme la récupération de configurations ou l'extraction de tables ARP d'un routeur.

- **Netmiko** : basé sur Paramiko, Netmiko simplifie les interactions avec les équipements en tenant compte des spécificités des constructeurs comme Cisco, Juniper ou HP. Il facilite la connexion, l'exécution de commandes et la gestion des erreurs.

- **NAPALM** : propose une interface unifiée pour gérer plusieurs fournisseurs (Cisco, Juniper, Arista, etc.). NAPALM permet de récupérer des données réseau, de charger des configurations ou de comparer des états réseau de manière standardisée, ce qui est très utile pour l'automatisation multi-vendeurs.

**Exemple** : Un script Python qui récupère automatiquement les configurations de centaines de routeurs et détecte les écarts par rapport à un modèle de référence.

---

## 2. Surveillance et gestion du réseau

Python est également excellent pour créer des outils de monitoring adaptés aux besoins spécifiques d'une entreprise.

- **Psutil** : permet de surveiller en temps réel l’utilisation CPU, la mémoire et les interfaces réseau des équipements. Utile pour construire des outils de supervision légère.

- **Scapy** : véritable couteau suisse de l’analyse réseau, Scapy permet de générer, manipuler, envoyer et intercepter des paquets réseau de nombreux protocoles. Les administrateurs peuvent ainsi réaliser du sniffing, de l’analyse de trafic ou même des tests de pénétration.

Ces outils permettent de développer des scripts capables de détecter des anomalies de trafic, mesurer la bande passante utilisée, alerter en cas de coupure, ou encore analyser en détail des incidents réseau.

**Exemple** : Un script Python qui analyse le trafic en temps réel et déclenche des alertes en cas de saturation de bande passante.

---

## 3. Frameworks d'automatisation avancés

Pour gérer de grandes infrastructures réseau, des frameworks avancés entièrement basés sur Python ont été développés :

- **Nornir** : contrairement à Ansible ou SaltStack, Nornir est directement programmé en Python, offrant une grande flexibilité. Il permet d'orchestrer l'exécution de tâches sur plusieurs équipements simultanément, de manipuler dynamiquement l'inventaire réseau et de personnaliser les workflows grâce à des plugins.

Nornir est idéal pour des environnements complexes nécessitant une grande précision dans le traitement des tâches ou pour les administrateurs préférant écrire des solutions sur-mesure.

---

## 4. Programmabilité et API réseau

Les fabricants d’équipements modernes (Cisco, Juniper, Arista, etc.) proposent des API ouvertes (REST, gRPC) pour configurer et superviser les équipements sans passer par le CLI. Python est très efficace pour utiliser ces APIs :

- **Requests** : permet de faire des appels API REST simples, parfait pour récupérer des informations ou envoyer des configurations.

- **gRPC Python** : pour interagir avec des APIs réseau performantes en temps réel.

- **pyATS (Cisco)** : une suite complète pour le test, la validation et l'automatisation de l'infrastructure réseau.

Les APIs permettent une programmabilité réseau complète, essentielle pour l'Infrastructure as Code (IaC).

---

## 5. Analyse prédictive et Machine Learning

Avec la montée en complexité des infrastructures réseau, l'analyse prédictive devient incontournable. Python, grâce à des bibliothèques comme Pandas, scikit-learn et TensorFlow, permet de :

- **Collecter et traiter** de grandes quantités de logs réseau.
- **Identifier** des modèles de comportement réseau normaux/anormaux.
- **Construire** des modèles prédictifs pour anticiper des incidents (panne d'équipement, congestion, attaque DDoS, etc.).

---

## 6. Monitoring avancé et visualisation

Python est aussi utilisé pour créer des tableaux de bord interactifs de supervision réseau :

- **Grafana** : intégré avec des scripts Python pour alimenter des dashboards en données temps réel.
- **Prometheus Exporters** en Python : pour extraire des métriques spécifiques d’équipements non supportés nativement.
- **Flask / Django** : création d’interfaces web de surveillance internes, sur-mesure selon les besoins de l’entreprise.

---

## 7. Sauvegarde automatique et gestion des migrations réseau

La sauvegarde régulière des configurations est critique pour toute infrastructure. Python permet d'automatiser :

- La connexion SSH/API aux équipements.
- La récupération de configurations.
- La sauvegarde dans un système de fichiers local ou un dépôt Git pour historiser les changements.

Python est également utilisé pour préparer et appliquer des migrations réseau (modifications de configuration à grande échelle) de manière fiable et reproductible.

---

## 8. Gestion dynamique de l'inventaire réseau

Une gestion d'inventaire réseau précise est cruciale pour la maintenance et la planification. Avec Python, il est possible de :

- Scanner dynamiquement les équipements (SNMP, SSH, API).
- Synchroniser l'inventaire avec des outils comme Netbox.
- Générer des rapports d’audit réguliers.

---

## 9. Usage personnel et en entreprise

En tant qu'apprenti administrateur réseau, cette veille technologique m’a inspiré plusieurs idées concrètes. Voici quelques usages de Python que j’aimerais mettre en pratique ou approfondir, aussi bien dans un cadre personnel que professionnel :


### Automatisation des tâches en entreprise

- **Sauvegarde automatique des configurations réseau :** développement d’un script Python utilisant Netmiko pour se connecter aux équipements Cisco déployés chez les clients, extraire automatiquement la configuration et l’enregistrer localement avec un horodatage.

### Supervision des machines

- **Surveillance du NAS interne et de ceux des clients** : utilisation de psutil pour suivre les indicateurs clés (espace disque, charge CPU/RAM…), avec génération automatique de rapports hebdomadaires.

- **Création d’un tableau de bord personnalisé** (avec Flask ou Streamlit) pour visualiser en temps réel les données de supervision depuis un navigateur web.


### Tests de sécurité basiques

- **Détection de ports ouverts :** script Python conçu pour scanner un réseau de test et identifier les services exposés, dans une optique de contrôle préventif (approche similaire à Nmap).

- **Vérification automatisée des configurations SSH :** script permettant de détecter les paramètres de sécurité faibles (ex. : authentification par mot de passe activée) sur les routeurs et serveurs clients.

---

## Conclusion

Grâce à cette veille, j’ai pu comprendre à quel point Python est un outil puissant et polyvalent pour le métier d’administrateur réseau. Que ce soit pour automatiser des tâches, surveiller des équipements, interagir avec des API ou encore analyser des données réseau, Python offre énormément de possibilités.

Ce qui est intéressant, c’est à quel point il peut simplifier le quotidien : on peut gagner du temps, éviter les erreurs, et rendre les opérations réseau beaucoup plus efficaces. Et surtout, on peut créer ses propres outils, adaptés à ses besoins.

Cette veille m’a aussi donné plein d’idées de projets que j’aimerais mettre en place, aussi bien dans mon entreprise qu’à titre personnel. Par exemple, automatiser les sauvegardes de configuration, surveiller l’état des serveurs ou tester la sécurité de certains équipements. Ce sont des choses concrètes que je peux développer avec Python.

En résumé, Python n’est pas juste un langage utile : c’est une vraie valeur ajoutée pour les administrateurs réseau d’aujourd’hui et de demain. C’est pour moi une compétence essentielle que je compte bien continuer à apprendre et à mettre en pratique.

---

## Sources

- [Comment utiliser Python pour automatiser le réseau | LeMagIT](https://www.lemagit.fr/conseil/Comment-utiliser-Python-pour-automatiser-le-reseau)
- [Administration système — The Hitchhiker's Guide to Python](https://python-guide-pt-br.readthedocs.io/fr/latest/scenarios/admin.html)
- [Initiation à SNMP avec Python : PySNMP (Partie 1) - Le protocole et les commandes | Makina Corpus](https://makina-corpus.com/python/initiation-snmp-avec-python-pysnmp-partie-1-le-protocole-et-les-commandes)

---

## Script Python qui fait un ipconfig

Cette partie n'a pas de lien direct avec cette veille, mais elle fait partie de mon projet de parseur markdown :
```python-exec
[Script d'exemple](ipconfig.py)
```
