datos=[]
print("¿Cuantos datos desea ingresar?")
cantidad=input("Ingrese la cantidad en numeros: ")
if cantidad.isdigit():
    for i in range(int(cantidad)):
        ingresar=i+1
        datos.append(int(ingresar))
print(f"Su lista es: {datos}")

