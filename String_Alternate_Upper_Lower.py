def myfunc(sampleStr):
    newStr = ''
    for i in range(len(sampleStr)):
        if(i%2==0):
            newStr+=sampleStr[i].lower()
        else:
            newStr+=sampleStr[i].upper()
    return newStr