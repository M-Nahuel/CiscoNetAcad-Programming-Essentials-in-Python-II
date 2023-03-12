def inp(prompt):
    str = input(prompt)
    if str == '':
        print('You have\'nt entered any word, try again!')
        inp(prompt)
    return str

def splitter(str):
    return str.split()

def loop(ls):
    str = ''
    for value in ls:
        str += value
    return str

def checker(value1, value2):
    if sorted(value1) == sorted(value2):
        return 'Son Anagramas'
    else:
        return 'No son Anagramas'

def anagram():
    firstW = inp('Enter the first word: ').lower()
    secondW = inp('Enter the second word: ').lower()
    
    list1 = splitter(firstW)
    list2 = splitter(secondW)
    
    firstW = loop(list1)
    secondW = loop(list2)
    
    if len(firstW) != len(secondW):
        return 'No son Anagramas'
    
    return checker(firstW, secondW)
    
print(anagram())