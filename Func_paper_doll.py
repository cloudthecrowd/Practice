# Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    newStr=''
    for i in range(len(text)):
        newStr+=text[i]*3
    return newStr