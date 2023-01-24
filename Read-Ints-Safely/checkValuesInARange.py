def readint(prompt, min, max):
    try:
        while True:
            x = int(input(prompt))
            assert x > min and min < max
            break
        return x
    except ValueError:
        print('Error: invalid input')
        v = readint(prompt, min, max)
    except AssertionError:
        print('Error: the value is out of allowed range')

v = readint("Enter a number between -10 a 10: ", -10, 10)

print("The number is:", v)
