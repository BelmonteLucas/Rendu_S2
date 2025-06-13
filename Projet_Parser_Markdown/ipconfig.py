
import datetime
import subprocess

print("Voici l'heure d'exécution de la commande ipconfig :")
print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# Exécuter ipconfig
resultat = subprocess.run(["ipconfig"], capture_output=True, text=True, shell=True, encoding='cp850')

# Afficher correctement
print(resultat.stdout)




