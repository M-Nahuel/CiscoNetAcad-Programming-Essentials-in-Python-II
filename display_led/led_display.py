def ledDisplay(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0:
                list = []
                for a in str(num):
                    list.append(int(a))
                    ls = [
                            ['###','  #','###','###','# #','###','###','###','###','###'],
                            ['# #','  #','  #','  #','# #','#  ','#  ','  #','# #','# #'],
                            ['# #','  #','###','###','###','###','###','  #','###','###'],
                            ['# #','  #','#  ','  #','  #','  #','# #','  #','# #','  #'],
                            ['###','  #','###','###','  #','###','###','  #','###','###']
                            ]
                    for r in range(5):
                        e = ' '
                        for i in range(len(list)):
                            if i == len(list)-1:
                                e = '\n'
                                print(ls[r][list[i]], end=e)
            else:
                ledDisplay(prompt)
        except ValueError:
            print('The input must be a non negative integer.\nPlease try again!')
            ledDisplay(prompt)

ledDisplay('Enter a non negative number: ')