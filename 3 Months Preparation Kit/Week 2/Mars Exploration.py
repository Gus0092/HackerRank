#https://www.hackerrank.com/challenges/Mars-Exploration/problem
#Dificuldade: Facil
def marsExploration(s):
    # Write your code here
    x = 0
    y = len(s)
    z = 0
    while x<y:
        if s[x] not in "S":
            z+=1
        if s[x+1] not in "O":
            z+=1
        if s[x+2] not in "S":
            z+=1
        x+=3
    return (z)