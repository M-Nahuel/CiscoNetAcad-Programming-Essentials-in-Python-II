def sudoku():
    list = [295743861, 431865927, 876192543, 387459216, 612387495, 549216738, 763524189, 928671354, 154938672]
    
    #Tester for the columns
    def ctester():
        for i in range(9):
            test = ''
            for k in range(9):
                test += list[k][j]
                if k == 8:
                    for l in range(9):
                        if test.find(l) == -1:
                            return False
        return True
    
    
    #for i in range(9):
    #    list.append([input('Ingrese 9 numeros para rellenar la fila: ')])
    
    for j in range(9):
        for k in range(9):
            print(list[j][k])
            if int(list[j][k]) > 9:
                return 'Los numeros ingresados no deben ser mayor a 9!'
            if list[j].find(k+1) == -1:
                return 'Los numeros no se deben repetir!'
    if ctester():
        return 'Si'
    
    
sudoku()
