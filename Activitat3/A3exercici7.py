# Amb while indicar si el número guardat a una variable està entre 100 i 400.

nombre = 100

while nombre >= 100 and nombre <= 400:
    nombre = int(input("Introdueix un valor: "))
    if nombre >= 100 and nombre <= 400:
        print(f'El número {nombre} està entre 100 i 400')