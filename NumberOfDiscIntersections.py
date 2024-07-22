# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    l = []
    r = []
    for x in range(len(A)):
        l.append(x - A[x])
        r.append(x+A[x])
    l.sort()
    r.sort()
    pointer = 0
    counter = 0 
    for x in range(0, len(A)):
        for y in range(pointer, len(A)):
            if l[y] > r[x]:
                break
            pointer += 1
        counter += pointer - (1+x)
        if counter > 1e7:
            return -1
    return counter
