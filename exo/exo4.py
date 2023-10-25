import random

nombres = [random.randint(1, 100) for _ in range(10)]

maximum = max(nombres)
minimum = min(nombres)

moyenne = sum(nombres) / len(nombres)

print("Liste de nombres : ", nombres)
print("Maximum : ", maximum)
print("Minimum : ", minimum)
print("Moyenne : ", moyenne)
