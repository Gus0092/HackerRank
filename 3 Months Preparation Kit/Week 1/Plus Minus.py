#https://www.hackerrank.com/challenges/plus-minus/problem
def plusMinus(arr):
    i = 0
    ng = 0
    ne = 0
    for x in arr:
        if x > 0:
            i +=1
        elif x < 0:
            ng +=1
        else:
            ne += 1
    print ("%.6f" % (i/len(arr)))
    print ("%.6f" % (ng/len(arr)))
    print ("%.6f" % (ne/len(arr)))