import re
import io
import sys

def executer_script(fichier_py):
    try:
        with open(fichier_py, "r", encoding="utf-8") as f:
            code = f.read()

        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        exec(code, {})
        
        sys.stdout = old_stdout
        return f"<pre>{buffer.getvalue()}</pre>"
    
    except Exception as e:
        sys.stdout = old_stdout
        return f"<pre>Erreur dans {fichier_py} : {e}</pre>"

def remplacer_liens_scripts(markdown_text):
    pattern = r"\[.*?\]\((.*?\.py)\)"
    
    def remplacer(match):
        fichier_py = match.group(1)
        return executer_script(fichier_py)
    
    new_text = re.sub(pattern, remplacer, markdown_text)
    return new_text


def transformer_line(texte):
    # Gras **texte** ou _texte_
    texte = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texte)
    texte = re.sub(r'_(.*?)_', r'<strong>\1</strong>', texte)
    # Liens [texte](url)
    texte = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', texte)
    # Images ![texte](url)
    texte = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', texte)
    return texte

def transformer_en_html(markdown_text):
    lignes = markdown_text.splitlines()
    html = []
    toc = []  # Table of Contents
    in_list = False
    in_code_block = False
    in_table = False

    for ligne in lignes:
        ligne = ligne.rstrip()

        if not ligne and not in_code_block:
            if in_list:
                html.append("</ul>")
                in_list = False
            if in_table:
                html.append("</table>")
                in_table = False
            continue

        # Blocs de code
        if ligne.strip().startswith("```"):
            if not in_code_block:
                html.append("<pre><code>")
                in_code_block = True
            else:
                html.append("</code></pre>")
                in_code_block = False
            continue

        if in_code_block:
            html.append(ligne)
            continue

        # Lignes de séparation
        if re.match(r'^(---|___|\*\*\*)$', ligne.strip()):
            html.append("<hr>")
            continue

        # Citations
        if ligne.strip().startswith("> "):
            citation = ligne.strip()[2:]
            html.append(f"<blockquote>{citation}</blockquote>")
            continue

        # Titres
        titre_match = re.match(r'^(#{1,6}) (.+)', ligne)
        if titre_match:
            niveau = len(titre_match.group(1))
            contenu = titre_match.group(2).strip()
            id_titre = contenu.lower().replace(" ", "-").replace("?", "").replace("!", "").replace(".", "").replace(",", "")
            toc.append(f'<li><a href="#{id_titre}">{contenu}</a></li>')
            html.append(f'<h{niveau} id="{id_titre}">{contenu}</h{niveau}>')
            continue

        # Listes
        if re.match(r'^(\*|-)\s+', ligne):
            if not in_list:
                html.append("<ul>")
                in_list = True
            item = ligne[2:].strip()
            html.append(f"<li>{transformer_line(item)}</li>")
            continue
        else:
            if in_list:
                html.append("</ul>")
                in_list = False

        # Autres paragraphes
        ligne = transformer_line(ligne)
        html.append(f"<p>{ligne}</p>")

    if in_list:
        html.append("</ul>")
    if in_table:
        html.append("</table>")

    # Générer le sommaire
    if toc:
        toc_html = "<nav id='toc'><h2>Sommaire</h2><ul>" + "\n".join(toc) + "</ul></nav><hr>"
        html.insert(2, toc_html)

    return "\n".join(html)

def ajouter_template(html_content):
    template = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Veille Python - Admin Réseau</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="container">
            {html_content}
        </div>

        <button id="top-button" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }});">
            ↑ Haut
        </button>

        <button id="bottom-button" onclick="window.scrollTo({{ top: document.body.scrollHeight, behavior: 'smooth' }});">
            ↓ Bas 
        </button>
    </body>
    </html>
    """
    return template


def main():
    with open("Veille_python.md", "r", encoding="utf-8") as f:
        markdown_text = f.read()

    markdown_avec_sorties = remplacer_liens_scripts(markdown_text)
    html_brut = transformer_en_html(markdown_avec_sorties)
    html_complet = ajouter_template(html_brut)

    # Ici : créer un fichier HTML
    with open("Veille_python_Lucas_BELMONTE.html", "w", encoding="utf-8") as f:
        f.write(html_complet)
if __name__ == "__main__":
    main()
