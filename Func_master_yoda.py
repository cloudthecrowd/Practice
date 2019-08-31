# Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    a=text.split()
    a=a[::-1]
    a=' '.join(a)
    print(a)