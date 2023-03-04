num = input('ingrese un numero entero no negativo: ')
list = []

for a in num:
    list.append(int(a))

ls = [
        ['###','  #','###','###','# #','###','###','###','###','###'],
        ['# #','  #','  #','  #','# #','#  ','#  ','  #','# #','# #'],
        ['# #','  #','###','###','###','###','###','  #','###','###'],
        ['# #','  #','#  ','  #','  #','  #','# #','  #','# #','  #'],
        ['###','  #','###','###','  #','###','###','  #','###','###']
     ]

for i in range(len(list)):
    e = ' '
    for row in range(5):
        for j in range(len(ls[row])):
            if j == 9:
                e = '\n'
            if j == list[i]:
                print(ls[row][j],i, sep=' ', end=e)

