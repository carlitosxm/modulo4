platos=[]
nombre=""

while True:
    print("\n--- Menú Principal ---")
    print("1. Añadir plato al menú")
    print("2. Buscar en el menú")
    print("3. Eliminar plato del menú")
    print("4. Mostrar platos del menú")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del plato: ")
        platos.append(nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del plato: ")
        validacion=nombre in platos
        if validacion==True:
            print("El plato existe en el menu")
        else:
            print("El plato no existe en el menu")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del plato: ")
        platos.remove(nombre)
    elif opcion == "4":
        print(platos)
    elif opcion == "5":
        print("Saliendo del programa. ¡Gracias por usar el sistema!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")