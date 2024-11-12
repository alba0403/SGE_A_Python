
salari = float(input("Introdueix el teu salari: "))

iva = 0  

if salari < 15000:
    iva = 0
elif salari < 30000:
    iva = 10
elif salari < 60000:
    iva = 21


import_iva = salari * iva / 100

# resultat
print(f"El teu salari és  de {salari} € i l'IVA aplicat és del {iva}%.")
print(f"L'import de l'IVA és de {import_iva} €.")