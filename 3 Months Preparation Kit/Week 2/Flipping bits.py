#https://www.hackerrank.com/challenges/Flipping-bits/problem
#Dificuldade: Facil
def flippingBits(n):
    # Write your code here
    x = 0
    y=0
    z=0
    while x<32:
        if n%2!=1:
            y=y+(10**x)
            z=z+(2**x)  
        x+=1
        n=int(n/2) 
    n = z
    return (n)