nombre_pacientes=[]
edades=[]

def agregar_nombre(datos):
    nombres=" ".join(datos.split()[:2])
    nombre_pacientes.append(nombres)
    
def agregar_edad(datos):
    edad = int(2025-int(datos.split()[-1]))
    edades.append(edad)

def imprimir():
    print(f" Lista de nombre: {nombre_pacientes}")
    print(f" Lista de edades: {edades}")
    menor=min(edades)
    indice_menor=edades.index(menor)
    mayor=max(edades)
    indice_mayor=edades.index(mayor)
    paciente_menor=nombre_pacientes[indice_menor]
    paciente_mayor=nombre_pacientes[indice_mayor]
    print(f"El Paciente menor es: {paciente_menor} con {menor} ")
    print(f"El paciente mayor es: {paciente_mayor} con {mayor}")