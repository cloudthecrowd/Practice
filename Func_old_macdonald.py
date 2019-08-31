# Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    newStr=''
    for i in range(len(name)):
        if i==0:
            newStr+=name[i].upper()
        elif i==3:    
            newStr+=name[i].upper()
        else:
            newStr+=name[i].lower()
    return newStr