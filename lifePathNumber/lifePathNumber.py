def digit():
    inp = input('Ingrese solamente los digitos de su fecha de cumpleaños: ')
    
    while True:
        if len(inp) > 1:
            su = 0
            ls = list(inp)
            for n in ls:
                su += int(n)
            inp = str(su)
        else:
            break
    return inp

print('El digito de la vida de su fecha de cumpleaños es: ' + digit())
