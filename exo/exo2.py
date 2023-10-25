phrase = input("Saisissez une phrase : ")

majuscules = phrase.upper()
minuscules = phrase.lower()

mots = phrase.split()
nombre_de_mots = len(mots)

print("En majuscules : " + majuscules)
print("En minuscules : " + minuscules)
print("Nombre de mots : " + str(nombre_de_mots))
