# Scan Réseau Local – Application Flask

Application web simple pour scanner un réseau local, afficher les appareils détectés (IP, MAC, marque) et visualiser les résultats via un graphique circulaire.

---

## Structure du Projet

  .  
├── app.py               # Fichier principal : Scan  
├── templates/  
│   └── index.html          # Interface utilisateur

---

## Fonctionnalités

- Scan réseau local avec ARP (via Scapy)
- Affichage des IP, MAC, marques, ping
- Graphique circulaire interactif des marques détectées
- Recherche dans la table d’appareils
- Export CSV des résultats
- Copie rapide des IPs visibles
- Réinitialisation rapide de l’interface

---

## Technologies utilisées

- Python 3
- Flask
- Scapy
- Bootstrap 5
- Chart.js
- Requests

---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/BelmonteLucas/Rendu_S2.git
cd Rendu_S2/Projet_Scanner_Reseau
```
2. Installer les dépendances :

```bash
pip install flask scapy requests
```
3. Lancer l’application :

```bash
python app.py
```
4. Ouvrir dans un navigateur :

```bash
http://localhost:5000
```
---

## Fichiers principaux

- app.py : logique Flask + scan ARP avec Scapy

- templates/index.html : interface utilisateur (Bootstrap, Chart.js, JS)

- README.md : documentation

---

## Fonctionnement

L’application utilise Scapy pour envoyer des requêtes ARP sur la plage IP fournie (ex : 192.168.1.1/24).
Les appareils actifs répondent avec leur adresse IP et MAC.
L’adresse MAC est ensuite utilisée pour détecter la marque via l’API gratuite https://api.macvendors.com/.

Les données sont :

- affichées dans un tableau

- comptabilisées pour générer un graphique circulaire

---

## Export CSV

Bouton "Télécharger CSV" pour sauvegarder tous les appareils détectés sous forme de fichier .csv.

---

## Limites & Remarques

Le scan ARP ne détecte que les appareils du sous-réseau local.

L’API macvendors.com peut retourner "Inconnu" si :

- La marque n’est pas connue

- Trop de requêtes ont été faites (limite API)

Le graphique ne s’affiche que s’il y a au moins un appareil détecté.

---

## Exemple d'utilisation :

![Scan](https://github.com/BelmonteLucas/Rendu_S2/blob/main/Projet_Scanner_Reseau/Image/Image_scan.png)

---

## Auteur

Lucas Belmonte - Projet de scan réseau - Python & Administration Réseau - 01 Juillet 2025

