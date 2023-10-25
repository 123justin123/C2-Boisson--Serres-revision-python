def tri_insertion(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle

ma_liste = [12, 11, 13, 5, 6]
tri_insertion(ma_liste)
print("Liste triée :", ma_liste)
