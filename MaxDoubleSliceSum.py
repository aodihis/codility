# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0:
        return

    m1 = [0] * len(A) 
    m2 = [0] * len(A)
    for x in range(1, len(A)-1):
        m1[x] = max(0, m1[x-1] + A[x])
    for x in range(len(A)-2, 0, -1):
        m2[x] = max(0, m2[x+1]+A[x])

    maxi = 0
    for x in range(1, len(A)-1):
        maxi = max(maxi,m1[x-1] + m2[x+1] )
    
    return maxi
