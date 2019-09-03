# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return ((abs(n-100)<=10) or (abs(n-200)<=10))