from empleado import EmpleadoMedioTiempo,EmpleadoTiempoCompleto

empleado1=EmpleadoTiempoCompleto("Carlos",500)
empleado2=EmpleadoMedioTiempo("Marco",300)

print(f"{empleado1.calcular_salario()}")
print(f"{empleado2.calcular_salario()}")

empleados=[empleado1,empleado2]
print("lista de empleados")
for empleado in empleados:
    print(f"Nombre: {empleado.nombre} Sueldo base: {empleado.salario_base} Sueldo bonificado: {empleado.calcular_salario()}")