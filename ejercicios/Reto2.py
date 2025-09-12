pais=int(input(" ¿Cual es tu destino? por favor ingresa\n 1 Ecuador \n 2 Colombia \n 3 Perú \n  Ingresa el numero: "))
zona=int(input(" ¿A que sona te dirijes? por favor ingresa\n 1 Zona urbana \n 2 Zona rural \n 3 Zona perimetral \n  Ingresa el numero: "))
velocidad=int(input("¿Cual es tu velocidad de en el zona? "))

if pais==1:
    if zona==1:
        if velocidad<10:
            print("Tu velocidad es menos a al minima 10Km/h")
        elif velocidad>50:
            print("Tu velocidad es mayor a la maxima 50Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
    elif zona==2:
        if velocidad<51:
            print("Tu velocidad es menos a al minima 51Km/h")
        elif velocidad>70:
            print("Tu velocidad es mayor a la maxima 70Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
    elif zona==3:
        if velocidad<71:
            print("Tu velocidad es menos a al minima 71Km/h")
        elif velocidad>90:
            print("Tu velocidad es mayor a la maxima 90Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
elif pais==2:
    if zona==1:
        if velocidad<10:
            print("Tu velocidad es menos a al minima 10Km/h")
        elif velocidad>30:
            print("Tu velocidad es mayor a la maxima 30Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
    elif zona==2:
        if velocidad<31:
            print("Tu velocidad es menos a al minima 31Km/h")
        elif velocidad>80:
            print("Tu velocidad es mayor a la maxima 80Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
    elif zona==3:
        if velocidad<81:
            print("Tu velocidad es menos a al minima 81Km/h")
        elif velocidad>100:
            print("Tu velocidad es mayor a la maxima 100Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
elif pais==3:
    if zona==1:
        if velocidad<10:
            print("Tu velocidad es menos a al minima 10Km/h")
        elif velocidad>40:
            print("Tu velocidad es mayor a la maxima 40Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
    elif zona==2:
        if velocidad<41:
            print("Tu velocidad es menos a al minima 41Km/h")
        elif velocidad>60:
            print("Tu velocidad es mayor a la maxima 60Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")
    elif zona==3:
        if velocidad<61:
            print("Tu velocidad es menos a al minima 61Km/h")
        elif velocidad>120:
            print("Tu velocidad es mayor a la maxima 120Km/h")
        else: 
            print("Tu velocidad se encuentra dentro del limite")