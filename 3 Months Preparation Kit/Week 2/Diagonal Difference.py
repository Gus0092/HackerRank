#https://www.hackerrank.com/challenges/Diagonal-Difference/problem
#Dificuldade: Facil
def diagonalDifference(arr):
    l = 0
    r = 0
    x=0
    
    for i in arr:
        y=0
        for j in i:
            if (x)==(y):
                l+=j
            if (x)==((len(i))-1)-(y):
                r+=j
            y+=1
        x+=1
    return (abs(r-l))