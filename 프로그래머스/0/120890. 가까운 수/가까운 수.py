def solution(array, n):
    answer = 0
    sub = []
    for a in array:
        sub.append((a, abs(n-a)))
    sub = sorted(sub, key=lambda x:(x[1],x[0]))
    return sub[0][0]