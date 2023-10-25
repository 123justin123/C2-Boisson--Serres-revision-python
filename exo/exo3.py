operation = input('Entrez une opération ex: (1 + 1) : ')
nb1, op, nb2 = operation.split()
nb1, nb2 = int(nb1), int(nb2)

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else "Division par zéro impossible"
}

if op in operations:
    resultat = operations[op](nb1, nb2)
    print(resultat)
else:
    print('Opération inconnue')
