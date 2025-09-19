from vehiculo import Vehiculo

class Moto (Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo=tipo

    def descripcion(self):
        informacion=super().descripcion()
        informacion.update({
            "Tipo ": self.tipo
        })
        return informacion