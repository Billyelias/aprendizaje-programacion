
def punto_reorden(d, lt, ss):
    # d: demanda diaria [u/dia], debe ser > 0
    # lt: lead time [dias], debe ser > 0
    # ss: stock de seguridad [u], puede ser 0 o mayor

    if d <= 0:
        raise ValueError('d debe ser mayor a 0')
    if lt <= 0:
        raise ValueError('lt debe ser mayor a 0')
    if ss < 0:
        raise ValueError('ss no puede ser menor que 0')

    return d*lt+ss

print(punto_reorden(40, 5, 30))
assert punto_reorden(40, 5, 30) == 230