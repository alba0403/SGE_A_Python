# Importar les dues classes que hem fet (Cotxe i Colibri)
from Cotxe import Cotxe
from Colibri import Colibri

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
cotxe_1.setColor("Vermell")
cotxe_2.setPreu(30000)

# Mostrar 2 atributs modificats de Cotxe a través dels getters
print(f'El meu cotxe és de color: {cotxe_1.getColor()}')
print(f'El meu cotxe val: {cotxe_2.getPreu()}')

# Modificar 2 atributs de Colibrí a través dels setters
colibri_1.setColor("Vermell")
colibri_2.setEdat(6)

# Mostrar 2 atributs modificats de Colibrí a través dels getters
print(f'El colibrí és de color {colibri_1.getColor()}')
print(f'Té {colibri_1.getEdat()} anys.')