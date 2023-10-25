nom_fichier_lecture = "fichier_source.txt"
nom_fichier_ecriture = "resultat.txt"

try:
    with open(nom_fichier_lecture, 'r') as fichier_source:
        contenu = fichier_source.read()
except FileNotFoundError:
    print(f"Le fichier {nom_fichier_lecture} n'a pas été trouvé.")
    exit(1)

mots = contenu.split()
nombre_de_mots = len(mots)

with open(nom_fichier_ecriture, 'w') as fichier_resultat:
    fichier_resultat.write(f"Le nombre de mots dans {nom_fichier_lecture} est : {nombre_de_mots}")

print(f"Le résultat a été écrit dans le fichier {nom_fichier_ecriture}.")
