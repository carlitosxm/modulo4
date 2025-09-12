import informacion
repetir=True
while repetir == True:
    nombre=input("Ingrese datos del paciente: Nombre Apellido Año_Nacimiento: ")
    informacion.agregar_nombre(nombre)
    informacion.agregar_edad(nombre)
    pregunta=input("Desea ingresar otros paciente (S/N): ")
    if pregunta == "N":
        repetir = False
        informacion.imprimir()