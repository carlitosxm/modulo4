from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio,num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas=num_puertas

    def descripcion(self):
        informacion=super().descripcion()
        informacion.update({
            "Numero de peurtas": self.num_puertas
        })
        return informacion