def readint(prompt, min, max):
    while True:
        try:
            x = int(input(prompt))
            assert x > min and x < max
            break
        except ValueError:
            print('Error: invalid input')
            v = readint(prompt, min, max)
        except AssertionError:
            print('Error: the value is out of allowed range')
    return x

v = readint("Enter a number between -10 a 10: ", -10, 10)

print("The number is:", v)
