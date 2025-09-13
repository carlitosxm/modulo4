from auto import auto

auto_toyota = auto.auto_nuevo()
auto_usado = auto.auto_usado("Ford", "Focus", 1990, 0)
mostrar_toyota = auto_toyota.mostrar_informacion()
mostrar_usado = auto_usado.mostrar_informacion()
print("¿Tienen el mismo kilometraje?", auto.validar_kilometraje(auto_toyota, auto_usado))
print("¿Es el auto usado antiguo?", auto.es_auto_antiguo(auto_usado))