
def calcular_oee(disp, rent, cal):
    # disp: disponibilidad [0-1] debe estar entre 0 y 1
    # rent: rentabilidad [0-1] debe estar entre 0 y 1
    # cal: calidad [0-1] debe estar entre 0 y 1

    if not 0 <= disp <= 1:
        raise ValueError('La disponibilidad debe estra entre 0 y 1')
    if not 0 <= rent <= 1:
        raise ValueError('La rentabilidad debe estar entre 0 y 1')
    if not 0 <= cal <= 1:
        raise ValueError('La calidad debe estar entre 0 y 1')

    return round(disp*rent*cal*100, 1)

assert calcular_oee(0, 0.9, 0.7) == 0
assert calcular_oee(1, 0.9, 0.9) == 81

print('los calculos del OEE pasaron las pruebas')

def clasificar_oee(valor):
    if not 0 <= valor <= 100:
        raise ValueError('El valor esta fuera del rango [0 - 100]')

    if valor >= 85:
        return 'Clase mundial'
    elif valor >= 60:
        return 'Aceptable'
    else:
        return 'Bajo'

assert clasificar_oee(100) == 'Clase mundial'
assert clasificar_oee(60) == 'Aceptable'
assert clasificar_oee(0) == 'Bajo'

print('Las clasificaciones pasaron al prueba')