def solution(strArr):
    answer = []
    for idx, st in enumerate(strArr):
        ans = ''
        for s in st:
            if not(idx % 2):
                ans += s.lower()
            else:
                ans += s.upper()
        answer.append(ans)
    return answer