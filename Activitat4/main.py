
from Cotxe import Cotxe

# Fer tres instàncies de l'objecte Cotxe
cotxe_1 = Cotxe("Blau", "Ford", 5, "Fiesta", 20000)
cotxe_2 = Cotxe("Gris", "BMW", 7, "Serie 2", 27000)
cotxe_3 = Cotxe("Negre", "Audi", 5, "A3", 17000)

# Fer tres instàncies de l'objecte Colibrí
colibri_1 = Colibri("verd", 2, 5, 4,"Colibrí rutilante")
colibri_2 = Colibri("lila", 3, 12, 5,"Colibrí oreja violeta")
colibri_3 = Colibri("marró", 5, 14, 4,"Colibrí pardo")

# Mostrar 3 getters de Cotxe
print(f'El meu cotxe és de color: {cotxe_1.getColor()}')
print(f'La seva marca és: {cotxe_1.getMarca()}')
print(f'I té {cotxe_1.getNum_seients()} seients.')

# Mostrar 4 getters de Colibrí
print(f'El colibrí és de color {colibri_1.getColor()}')
print(f'Té {colibri_1.getEdat()} anys.')
print(f'La seva mida és de {colibri_1.getMida()} cm.')
print(f'I pesa uns {colibri_1.getPes()} grams.')

# Modificar 2 atributs de Cotxe a través dels setters


# Mostrar 2 atributs modificats de Cotxe a través dels getters


# Modificar 2 atributs de Colibrí a través dels setters


# Mostrar 2 atributs modificats de Colibrí a través dels getters
