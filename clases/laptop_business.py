import random
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria,almacenamiento,duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento=almacenamiento
        self.duracion_bateria=duracion_bateria

    def __str__(self):
        return f"Marca: {self.marca} \n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Almacenamiento: {self.almacenamiento}\n Bateria: {self.duracion_bateria}\n Costo: {self.costo}\n Impuesto: {self.impuesto}"


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

    def realizar_informe_uso(self):
        informe=super().realizar_informe_uso()
        informe.update({
            "Tipo":"Gaming",
            "Uso Recoemndado":"Juegos de video",
            "Horas de uso":10,
            "Recomendaciones de software":["Antivirus","VPN"]
        })
        return informe
