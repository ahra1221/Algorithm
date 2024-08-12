def solution(n):
    answer = 0
    d = [0] * 2000
    d[0] = 0
    d[1] = 1
    d[2] = 2
    if n > 2:
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
    return d[n] % 1234567