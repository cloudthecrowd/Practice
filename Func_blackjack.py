# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum((a,b,c))<=21:
        return sum((a,b,c));
    elif total>21 and 11 in (a,b,c):
        return sum((a,b,c))-10
    else:
        return 'Bust'