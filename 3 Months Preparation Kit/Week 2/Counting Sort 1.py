#https://www.hackerrank.com/challenges/countingsort1/problem
#Dificuldade: Facil
def countingSort(arr):
    # Write your code here
    x=0
    y=[]
    while (x)< (100):
        y.insert(x,0)
        x+=1
    for i in arr:
        y[i]+=1
    return (y)