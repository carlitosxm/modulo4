class auto:
    def __init__(self,marca, modelo,anio,kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=kilometraje

    def mostrar_informacion(self):
        return print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometraje}")
    
    def actualizar_kilometraje(self, kilometros):
        if (kilometros<self.kilometraje):
            print("El kilometraje no puede ser menor al del registro anterior")
        else:
            self.kilometraje=kilometros
            print(f"Kilometraje actualizado a {self.kilometraje}")
    
    def realizar_viaje(self, kilometros):
        self.kilometraje+=kilometros

    def estado_auto(self):
        if(self.kilometraje<20000):
            print("Estoy como nuevo")
        elif(self.kilometraje<100001):
            print("Ya estoy usado")
        elif(self.kilometraje>100000):
            print("Ya déjame descansar por favor!")
        
carro = auto("KIA","SOLUTO","2020") 
carro.mostrar_informacion()
carro.actualizar_kilometraje(1000)
carro.realizar_viaje(2000)
carro.estado_auto()
carro.mostrar_informacion()