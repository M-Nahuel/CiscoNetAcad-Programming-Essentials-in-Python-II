def palindrome(prompt):
    text = input(prompt)

    if text == '':
        print('You\'ve entered an empty string.')
        palindome(prompt)

    text = text.upper()
    
    text2 = text[len(text)//2:]

    for i in range((len(text)//2)+1, 0, -1):
        print(text[i+1])
        if text[i+1] != text2[i-1]:
            status = 'No es un palindromo'
            break
        else:
            status = 'Es un palindromo'
    print(status)

palindrome('Ingrese un texto: ')
