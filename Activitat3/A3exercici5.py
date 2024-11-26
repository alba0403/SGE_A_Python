# Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
suma = 0

print('parells:')
for i in num:
        if i % 2 == 0:
            suma = suma + i
print(suma)
            
suma = 0
print('senars:')
for i in num:
    if i % 2 == 1:
        suma = suma + i
print(suma)