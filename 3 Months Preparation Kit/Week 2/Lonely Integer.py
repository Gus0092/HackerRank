#https://www.hackerrank.com/challenges/lonely-integer/problem
def lonelyinteger(a):
    for x in a:
        c=0
        for y in a:
            if y == x:
                c+=1
        if c == 1:
            return x 