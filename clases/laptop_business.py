import random
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria,almacenamiento,duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento=almacenamiento
        self.duracion_bateria=duracion_bateria

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_diagnostico.update({
        "Resultado de red": self.verificar_conectividad_red(),
        "Almacenamiento": self.verificar_almacenamiento(),
        "Duración de batería": self.verificar_duracion_bateria()
    })
        return resultado_diagnostico
    
    def verificar_conectividad_red(self):
        resultado_red = {}
        if random.choice([True, False]):
            resultado_red["Wi-Fi disponible"] = True
        else:
            resultado_red["Wi-Fi disponible"] = False
        if random.choice([True, False]):
            resultado_red["Acceso a servidores empresariales"] = True
        else:
            resultado_red["Acceso a servidores empresariales"] = False
        if random.choice([True, False]):
            resultado_red["Latencia de red aceptable"] = True
        else:
            resultado_red["Latencia de red aceptable"] = False
        return resultado_red
    
    def verificar_almacenamiento(self):
        if self.almacenamiento < 500:
            return "Agregar mas almacenamiento"
        else:
            return "OK"
        
    def verificar_duracion_bateria(self):
        if self.duracion_bateria < 3:
            return "Duracion de bateria muy baja"
        else:
            return "OK"

