from laptop import Laptop

class Laptop_Gaming(Laptop):
    def __init__(self, marca, procesador, memoria, tarj_grafica, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarj_grafica = tarj_grafica

    def __str__(self):
        return f"Marca: {self.marca} \n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Tarjeta Grafica: {self.tarj_grafica}\n Costo: {self.costo}\n Impuesto: {self.impuesto}"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostivo = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostivo["Resultado juegos"] = resultado_juegos
        return resultado_diagnostivo
    
    def realizar_diagnostico_juegos(self):
        juegos = ["FORNITE","COD","GTA"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX"in self.tarj_grafica:
                fps=fps_base *3
            elif "GTX" in self.tarj_grafica:
                fps=fps_base *2
            else:
                fps = fps_base
            
            resultados [juego] = f"{fps} FPS"
        return resultados
    
    def realizar_informe_uso(self):
        informe=super().realizar_informe_uso()
        informe.update({
            "Tipo":"Gaming",
            "Uso Recoemndado":"Juegos de video",
            "Horas de uso":10,
            "Recomendaciones de software":["Antivirus","VPN"]
        })
        return informe