def palindrome(prompt):
    text = input(prompt)

    if text == '':
        print('You\'ve entered an empty string.')
        palindome(prompt)

    text = text.split()
    text2 = ''
    for word in text:
        text2 += word
    text2 = text2.lower()
    
    if len(text2) % 2 == 1:
        end = (len(text2)//2)+1
    else:
        end = len(text2)//2

    status = 'Es un palindromo'
    for index in range(len(text2), end, -1):
        if text2[index-1] != text2[len(text2)-index]:
            status = 'No es un palindromo'
            return status
    
    return status


print(palindrome('Ingrese un texto: '))
