def solution(msg):
    answer = []
    d = {chr(k):k-64 for k in range(65,91)}
    w = ''
    c = w
    num = 27
    for m in msg:
        c  = w + m
        if c in d:
            w = c
        else:
            answer.append(d[w])
            d[c] = num
            num += 1
            w = m
    if w in d:
        answer.append(d[w])
    return answer