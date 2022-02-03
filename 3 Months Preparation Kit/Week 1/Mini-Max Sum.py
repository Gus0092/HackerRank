#https://www.hackerrank.com/challenges/mini-max-sum/problem
def miniMaxSum(arr):
    ma = 0
    mi = 0
    arr = sorted(arr)    
    mi = sum (arr[0:4])
    ma = sum (arr[1:5])
    print ("%d %d" % (mi,ma))