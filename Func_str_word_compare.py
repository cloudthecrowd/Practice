# Write a function takes a two-word string and returns True if both words begin with same letter

def myfunc(sampleStr):
    sampleStr=sampleStr.lower()
    a=sampleStr.split()
    if a[0][0]==a[1][0]:
        print(True)
    else:
        print(False)