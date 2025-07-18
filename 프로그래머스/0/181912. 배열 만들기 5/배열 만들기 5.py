def solution(intStrs, k, s, l):
    answer = []
    for st in intStrs:
        tmp = int(st[s:s+l])
        print(tmp)
        if tmp > k:
            answer.append(tmp)
    return answer