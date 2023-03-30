def sudoku():
    ls = []
    for i in range(9):
        ls.append([input('Ingrese 9 numeros para rellenar la fila: ')])
    
    #Tester for the columns
    def ctester(ls):
        for i in range(9):
            sample = ''
            for k in range(9):
                sample += ls[k][i]
            for l in range(9):
                if sample.find(str(l+1)) == -1:
                    return False
        return True
    
    #Tester for the rows
    def rtester(ls):
        for i in range(9):
            sample = ''
            for k in range(9):
                sample += ls[i][k]
            for l in range(9):
                if sample.find(str(l+1)) == -1:
                    return False
        return True
    
    #Tester for the 3 x 3 box
    def btester(ls):
        for i in range(0,9,3):
            for j in range(0,9,3):
                checker = []
                for k in range(3):
                    for l in range(3):
                        checker.append(ls[i+k][j+l])
        for l in range(9):
            if str(l+1) not in checker:
                return False
        return True
        
        
    if (ctester(ls) and rtester(ls) and btester(ls)):
        return 'Si'
    else:
        return 'No'
    
print(sudoku())
