# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def compare(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)