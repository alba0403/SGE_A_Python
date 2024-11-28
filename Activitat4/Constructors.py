#Crear una classe de nom Cotxe amb un constructor que contingui 5 paràmetres i caldrà escriure tots els getters/Setters necessaris per a actualitzar i modificar tots els paràmetres.

class Cotxe:
    # Constructor
    def __init__(self, color, marca, num_seients, model, preu):
        #Atributs
        self.color = color
        self.marca = marca
        self.num_seients = num_seients
        self.model = model
        self.preu = preu
    
    # Getters i Setters
    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color
        
    def getMarca(self):
        return self.marca
    def setMarca(self, new_marca):
        self.marca = new_marca
        
    def getNum_seients(self):
        return self.num_seients
    def setNum_seients(self, new_num_seients):
        self.num_seients = new_num_seients
    
    def getModel(self):
        return self.model
    def setModel(self, new_model):
        self.model = new_model
        
    def getPreu(self):
        return self.preu
    def setPreu(self, new_preu):
        self.preu = new_preu


class Colibri:
    # Constructor
    def __init__(self, color, edat, mida, pes, especie):
        #Atributs
        self.color = color
        self.edat = edat
        self.mida = mida
        self.pes = pes
        self.especie = especie
    
    # Getters i Setters
    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color
        
    def getEdat(self):
        return self.edat
    def setEdat(self, new_edat):
        self.edat = new_edat
        
    def getMida(self):
        return self.mida
    def setMida(self, new_mida):
        self.mida = new_mida
    
    def getPes(self):
        return self.pes
    def setPes(self, new_pes):
        self.pes = new_pes
        
    def getEspecie(self):
        return self.especie
    def setEspecie(self, new_especie):
        self.especie = new_especie