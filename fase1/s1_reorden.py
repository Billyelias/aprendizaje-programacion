
def punto_reorden (d, lt, ss):
    if d <= 0:
        raise ValueError('d debe ser mayor a 0')
    if lt <= 0:
        raise ValueError('lt debe ser mayor a 0')
    if ss < 0:
        raise ValueError('ss no puede ser menor que 0')

    return d*lt+ss

print(punto_reorden(40, 5, 30))
assert punto_reorden(40, 5, 30) == 230