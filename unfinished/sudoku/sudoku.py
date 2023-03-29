def sudoku():
    list = ['195743862', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '254938671']
    
    #Tester for the columns
    def ctester():
        for i in range(9):
            test = ''
            for k in range(9):
                test += list[k][j]
                if int(k) == 8:
                    for l in range(9):
                        if test.find(str(l+1)) == -1:
                            return False
        return True
    #Tester for the 3 x 3 box
    def btester():
        for i in range(0,9,3):
            for j in range(0,9,3):
                checker = []
                for k in range(3):
                    for l in range(3):
                        checker.append(list[i+k][j+l])
        for a in range(9):
            if str(a) not in checker:
                return 'No'
    btester()
    
    #for i in range(9):
    #    list.append([input('Ingrese 9 numeros para rellenar la fila: ')])
    
    for j in range(9):
        for k in range(9):
            print(list[j][k],end=' ')
            if int(list[j][k]) > 9:
                return 'Los numeros ingresados no deben ser mayor a 9!'
            if list[j].find(str(k+1)) == -1:
                return 'Los numeros no se deben repetir!'
        print()
    if ctester():
        return 'Si'
    
print(sudoku())
