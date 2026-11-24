
def calcular_oee(disp, rend, cal):
    # disp: la disponibilidad [0-1] debe estar entre 0 y 1
    # rend: el rendimiento [0-1] debe estar entre 0 y 1
    # cal: la calidad [0-1] debe estar entre 0 y 1

    if not 0 <= disp <= 1:
        raise ValueError('La disponibilidad debe estar entre 0 y 1')

    if not 0 <= rend <= 1:
        raise ValueError('El rendimiento debe estar entre 0 y 1')

    if not 0 <= cal <= 1:
        raise ValueError('La calidad debe estar entre 0 y 1')
    
    return round((disp*rend*cal)*100, 1)

def clasificar_oee(oee_pct):
    # oee_pct: OEE en porcentaje [%], debe estar entre 0 y 100
    if not 0 <= oee_pct <= 100:
        raise ValueError('El OEE debe estar entre 0 y 100')

    if oee_pct >= 85:
        return 'Clase mundial'
    elif oee_pct >= 60:
        return 'Aceptable'
    else:
        return 'Bajo'


print(clasificar_oee(calcular_oee(0.9, 0.8, 0.9)))

assert calcular_oee(0.9, 0.7, 0.4) == 25.2
assert calcular_oee(0.9, 0.6, 1) == 54
assert calcular_oee(0.9, 0.85, 0.97) == 74.2
assert calcular_oee(1.2, 0.9, 0.9) # Error en disponibilidad, sale del rango permitido [0-1]

assert clasificar_oee(90) == 'Clase mundial'
assert clasificar_oee(100) == 'Clase mundial'
assert clasificar_oee(40) == 'Bajo'
assert clasificar_oee(85) == 'Clase mundial'
assert clasificar_oee(60) == 'Aceptable'
assert clasificar_oee(150) # Error en valor de OEE, sobrepasa el limite establecido (100)
print('todas las pruebas pasaron')