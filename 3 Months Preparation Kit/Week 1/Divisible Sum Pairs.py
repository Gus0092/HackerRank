#https://www.hackerrank.com/challenges/Divisible-Sum-Pairs/problem
def divisibleSumPairs(n, k, ar):
    x = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                x =x+1
    return x