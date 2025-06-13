import re
import io
import sys
import markdown

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

def transformer_en_html(markdown_text):
    return markdown.markdown(markdown_text)

def ajouter_template(html_content):
    template = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Veille Python - Admin Réseau</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 2rem;
                line-height: 1.6;
            }}
            h1, h2, h3 {{
                color: #333;
                text-align: center;
            }}
            p, li {{
                color: #555;
            }}
            pre {{
                background: #272822;
                color: #f8f8f2;
                padding: 1rem;
                border-radius: 5px;
                overflow-x: auto;
            }}
            a {{
                color: #007acc;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .container {{
                max-width: 900px;
                margin: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {html_content}
        </div>
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
    with open("Veille_python.html", "w", encoding="utf-8") as f:
        f.write(html_complet)


if __name__ == "__main__":
    main()
