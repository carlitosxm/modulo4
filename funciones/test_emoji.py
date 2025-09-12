import emoji

cantidad_frese = int(input ("Cuantas fraases sea ingresar "))
for i in range(cantidad_frese):
    frase=input("Ingrese la frase")
    emoji.encontrar_palabra(frase)
    emoji.agregar_frase(frase)