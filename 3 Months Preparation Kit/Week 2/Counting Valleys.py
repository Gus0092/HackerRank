#https://www.hackerrank.com/challenges/Counting-Valleys/problem
#Dificuldade: Facil
def countingValleys(steps, path):
    # Write your code here
    x=0
    y=0
    for i in path:
        if i == "U":
            x+=1
            if x==0:
                y+=1            
        else:
            x-=1       
    return (y) 