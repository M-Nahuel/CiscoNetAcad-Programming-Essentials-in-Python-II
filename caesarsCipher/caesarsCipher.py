#Caesars Cipher

text = input('Ingresa tu mensaje: ')
while True:
        value = input('Ingresa un valor de cambio entre 1 y 25: ')
        if value.isdigit():
            value = int(value)
            if value not in range(1, 26):
                print('El valor ingresado debe estar entre 1 y 25')
                continue
            break
        else:
            print('El valor ingresado debe ser un entero')

cipher = ''

def upper(ch):
    if ch > ord('Z') - value:
        temp = ch + value - ord('Z') -1
        return chr(ord('A') + temp)
    return chr(ch + value)

def lower(ch):
    if ch > ord('z') - value:
        temp = ch + value - ord('z')-1
        return chr(ord('a')+ temp)
    return chr(ch + value)

for char in text:
    if not char.isalpha():
        cipher += char
        continue
    if char.isupper():
        cipher += upper(ord(char))
    else:
        cipher += lower(ord(char))
    
print(cipher)
