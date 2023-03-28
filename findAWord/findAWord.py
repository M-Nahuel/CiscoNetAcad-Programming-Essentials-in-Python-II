def finder():
    str = input('Ingrese la cadena en la que desea realizar la busqueda: ').lower()
    sbstr = input('Ingrese la palabra que desea buscar: ').lower()
    
    for i in sbstr:
        start = 0
        end = len(str)
        
        test = str.find(i,start,end)
        if test != -1:
            start = test
        else:
            return 'No'

    return 'Si'



print(finder())
