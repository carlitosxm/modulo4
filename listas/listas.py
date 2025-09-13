planetas=["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno"]
# print(planetas[-1])
# print(planetas[1: ])
# print(len(planetas))

gravedad_en_planetas = [0.378,0.907,1,0.377,2.36,0.916,0.889,1.12]
peso_bus = 124054

print(f"en la tierra un autobus de 2 pisos pesa {peso_bus} N")
print(f"En mercuerio un autobus de 2 pisos pesa {peso_bus*gravedad_en_planetas[0]} N")
print(f"lo mas liviano que seria un autobus en el sistema solar es {peso_bus*min(gravedad_en_planetas)} N")
print(f"lo mas pesado que seria un autobus en el sistema solar es {peso_bus*max(gravedad_en_planetas)} N")