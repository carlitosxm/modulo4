from vehiculo import Vehiculo
from auto import Auto
from moto import Moto


auto=Auto("KIA","SOLUTO",2020,4)
moto=Moto("SUZUKI","MODELO",2025,"DEPORTIVA")

print(auto.descripcion())
print(moto.descripcion())


vehiculos = [auto, moto]
for vehiculo in vehiculos:
    print(vehiculo.descripcion())