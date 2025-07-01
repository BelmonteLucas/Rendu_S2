# Parseur Markdown vers HTML avec exécution de scripts Python

## Objectif

Ce projet transforme un fichier Markdown (.md) en une page HTML complète et stylisée. Il ajoute la fonctionnalité d'exécuter dynamiquement les scripts Python liés dans le Markdown (liens vers fichiers .py) et d'injecter leur sortie dans le HTML final.

---

## Structure du Projet

 .  
├── main.py               # Fichier principal : conversion Markdown → HTML  
├── ipconfig.py        # Script Python utilisé dans le Markdown  
├── Veille_python.md         # Fichier Markdown source  
├── Veille_python_Lucas_BELMONTE.html  # Fichier HTML généré  
└── style.css                # Feuille de style CSS du rendu HTML

---

## Fonctionnalités

### Conversion Markdown → HTML

Le parseur gère les éléments Markdown suivants :

- Titres (#, ##, ..., ######)

- Texte en gras (**texte** ou _texte_)

- Liens texte

- Images 

- Listes * ou -

- Citations  

- Séparateurs 

- Blocs de code

---

## Exécution de scripts Python

Lorsqu’un lien vers un fichier .py est présent dans le Markdown, le script est exécuté au moment de la conversion, et sa sortie est injectée dans le HTML.

---

## Table des matières

Une table des matières est générée automatiquement à partir des titres du document.

---

## Mise en page stylisée

Une feuille de style (style.css) est appliquée au HTML pour :

- Titres centrés

- Thème clair

- Code coloré sur fond sombre

- Boutons haut/bas

- Citations, listes, tables bien présentées

---

## Détail des fichiers

### main.py :

Script principal. Fonctions clés :

- executer_script(fichier_py) : lit et exécute un script Python, retourne la sortie.

- remplacer_liens_scripts(markdown_text) : remplace les liens .py par les sorties des scripts.

- transformer_line(texte) : traite les éléments inline Markdown.

- transformer_en_html(markdown_text) : transforme les lignes Markdown en HTML.

- ajouter_template(html_content) : encapsule le contenu HTML avec un template.

- main() : lit le .md, convertit, génère le fichier HTML final.

### Veille_python.md :

Fichier Markdown source contenant du contenu à convertir.

### ipconfig.py :

Script Python d’exemple : ici, il exécute la commande réseau ipconfig et affiche l’heure à laquelle la commande a été lancée

---

## Utilisation

Rédiger un fichier Veille_python.md avec du Markdown.

Y inclure des liens vers des scripts Python si souhaité.

Lancer :

```bash
python main.py
```
Le fichier Veille_python_Lucas_BELMONTE.html est généré dans le répertoire courant.

---

## Auteur

Lucas Belmonte - Projet de veille technologique - Python & Administration Réseau - 01 Juillet 2025


