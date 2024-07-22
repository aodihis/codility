def solution(N, A):
    cx = [0] * N
    upper = 0

    maxi = 0
    for x in A:
        if x == N + 1:
            upper = maxi
            continue
        cx[x - 1] = max((upper + 1), (cx[x-1] + 1))
        maxi = max(cx[x-1], maxi)

    for x in range(0,len(cx)):
        cx[x] = max(upper, cx[x])
    return cx
