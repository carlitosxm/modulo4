from datetime import datetime

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
        
    @classmethod
    def auto_nuevo(cls):
        marca="Toyota"
        modelo="Hylux"
        anio=datetime.now().year
        return cls(marca="Toyota", modelo="Hylux", anio=datetime.now().year, kilometraje=0)

    @staticmethod
    def validar_kilometraje(auto1,auto2):
        if auto1.kilometraje==auto2.kilometraje:
            return "el kilometraje es igual"
        else:
            return "el kilometraje es diferente"

    @classmethod
    def auto_usado(cls, marca, modelo, anio, kilometraje):
        marca=marca
        modelo=modelo
        anio=anio
        kilometraje=kilometraje
        return cls(marca=marca, modelo=modelo, anio=anio, kilometraje=kilometraje)

    @staticmethod
    def es_auto_antiguo(auto):
        anio_actual = datetime.now().year
        if anio_actual > auto.anio:
            return "Es antiguo"
        else:
            return "No es antiguo"
 

#carro = auto("KIA","SOLUTO","2020") 
#carro.actualizar_kilometraje(1000)
#carro.realizar_viaje(2000)
#carro.estado_auto()
#carro.mostrar_informacion()
#carro.mostrar_informacion()