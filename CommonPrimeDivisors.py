# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def check(a,b):
    # print(f"a : {a}, b: {b}")
    if a == b:
        return 1
    a = a//b
    gcd_a_b = gcd(a, b)
    if gcd_a_b == 1:
        return -1
    return check(a, gcd_a_b)
    

def solution(A, B):
    tot = 0
    n = len(A)
    for x in range(n):
        if A[x] == B[x]:
            tot += 1
            continue

        if (A[x] == 1) or (B[x] == 1):
            continue
            
        a = A[x]
        b = B[x]
        gcd_val = gcd(a, b)

        a_r = check(a, gcd_val)
        if (a_r == -1):
            continue
        b_r = check(b, gcd_val)
        if (b_r == -1):
            continue 
        tot += 1
    
    return(tot)
