#https://www.hackerrank.com/challenges/Sparse-Arrays/problem
def matchingStrings(strings, queries):
    ar=[]
    for i in queries:
        x=0
        for j in strings:
            if i == j:
                x+=1
        ar.append(x)
    return (ar)
    