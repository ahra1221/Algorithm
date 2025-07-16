def solution(l, r):
    answer = []
    for i in range(l, r+1):
        i = str(i)
        ch = True
        for tmp in i:
            if (tmp !='0' and tmp != '5'):
                ch = False
                break
        if ch:
            answer.append(int(i))
    if not answer:
        return [-1]
    return answer