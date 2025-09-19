class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio

    def descripcion(self):
        resultado = {
            "MARCA" :f"{self.marca}",
            "MODELO" : f"{self.modelo}",
            "AÑO" : f"{self.anio}" 
        }
        return resultado