notes_eleves = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "David": 78,
    "Eve": 98
}

meilleur_eleve = max(notes_eleves, key=notes_eleves.get)
meilleure_note = notes_eleves[meilleur_eleve]

print(f"L'élève avec la meilleure note est {meilleur_eleve} avec une note de {meilleure_note}.")
