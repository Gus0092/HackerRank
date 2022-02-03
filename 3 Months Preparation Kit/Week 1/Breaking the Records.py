#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def breakingRecords(scores):
    mi = -1
    mir = 10**9
    ma = -1
    mar = -1
    for x in scores:
        if x > mar:
            ma+=1
            mar = x
        if x < mir:
            mi+=1
            mir = x
    
    return (ma, mi)