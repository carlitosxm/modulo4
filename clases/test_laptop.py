from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business


#laptop_pepito = Laptop("Lenovo","I7",32)
#laptop_maria = Laptop("Lenovo","I7",32,600)


#for numero in range(1,1001):
#    asus_laptop = Laptop.asus_laptop(numero)
#    print(asus_laptop.__dict__)

#print(Laptop.compara_costo(laptop_pepito,laptop_maria))

#print(laptop_pepito.__dict__)
#print(laptop_pepito.valor_final())
#print(laptop_pepito.valor_descuento(10))

#laptop_juanito=Laptop_Gaming("MSI","I7",64,"RTX 8GB")
#print(laptop_juanito.realizar_diagnostico_sistema())

laptop_carlos=Laptop_Business("HP","I5",16,512,2)
print(laptop_carlos.realizar_diagnostico_sistema())