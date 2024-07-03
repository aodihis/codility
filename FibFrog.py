# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.append(1)
    fibo = [0, 1]
    n = len(A)

    for x in range(2, n+2):
        val = fibo[x-1] + fibo[x-2]
        if val > n:
            break
        fibo.append(val)
        
    moves = [0] * (n)

    for x in fibo[1:]:
        if A[x -1] == 1:
            moves[x - 1] = 1

    if moves[-1] > 0:
        return moves[-1]

    for index in range(n):
        if A[index] == 0:
            continue
        if moves[index] == 0:
            continue
        current_move = moves[index]
        for x in fibo:
            next_point = x + index
            if next_point > n-1:
                break
            if A[next_point] == 0:
                continue
            if moves[next_point] == 0:
                moves[next_point] = current_move + 1
                continue
            moves[next_point] = min(moves[next_point], current_move + 1)

    if moves[-1] == 0:
        return -1
    return moves[-1]
