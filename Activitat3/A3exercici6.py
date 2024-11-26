# Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.

suma = 0
nombre = 0

while nombre >= 0 and nombre <= 100 and suma <= 100:
    nombre = int(input("Introdueix un valor: "))
    suma = suma + nombre
    if suma <= 100:
        print(suma)
    
