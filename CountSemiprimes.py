# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    prime = [0] * (N+1)
    
    semiprime = prime.copy()
    prime[0] = prime[1] = 1
    i = 2
    while (i <= N):
        if prime[i] == 0:
            x = i + i
            k = i * i 
            while x <= k and x <= N:
                div =  x//i
                if prime[div] == 0:
                    semiprime[x] = 1
                x += i
            while(k <= N):
                prime[k] = 1
                k+=i
        i += 1
    
    sum_semi = [0] * (N+1)
    for x in range(1,N+1):
        sum_semi[x] = sum_semi[x-1] + semiprime[x]

    res = []
    for x in range(0, len(P)):
        res.append(sum_semi[Q[x]] - sum_semi[P[x] -1])
    return(res)
