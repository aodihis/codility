# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    max_a = 2*n
    count = [0] * (max_a + 1)
    div = count.copy()

    for x in A:
        count[x] += 1
    
    for x in range(1, len(div)):
        if x*x >= len(div):
            break
        y = x * x
        while (y < len(div)):
            div[y] += count[x]
            if (y != x*x):
                div[y] += count[y//x]
            y += x
            
    
    res = []
    for x in A:
        non_div = n - div[x]
        res.append(non_div)
    return(res)
