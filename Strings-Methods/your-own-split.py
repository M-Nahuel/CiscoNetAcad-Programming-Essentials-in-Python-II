def misplit(strng):
#
    list = []
    if strng.isdigit():
        return 'The value entered should be a string'
    else:
        if(strng.isspace()):
            return list
        else:
            if(len(strng) == 0):
                return list
            else:
                strng = strng.lstrip()
                strng = strng.rstrip()
                index = 0
                for i in range(len(strng)):
                    if strng[i] == ' ':
                        list.append(strng[index : i])
                        index = i+1
                list.append(strng[index:])

                return list

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
