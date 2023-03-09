#Procesador de números
def numProcessor(prompt = 'Ingresa una línea de números, sepáralos con espacios: '):
    while True:
        linea = input(prompt)
        if linea is not '':
            break

    strings = linea.split()
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        print("El total es:", total)
    except:
        print(substr, "no es un numero.")

numProcessor()
