#https://www.hackerrank.com/challenges/flipping-the-matrix/problem
#Dificuldade: Medium
def flippingMatrix(matrix):
    m= matrix
    l = int(len(matrix[0]))-1
    n = int(l/2)
    y = 0
    o = 0
    while y <= n:
        x=0
        while x <= n:
            o+=max(m[y][x],m[y][l-x],m[l-y][x],m[l-y][l-x])
            print(o)
            print(n)
            x+=1                
        y+=1 
    return (o) 