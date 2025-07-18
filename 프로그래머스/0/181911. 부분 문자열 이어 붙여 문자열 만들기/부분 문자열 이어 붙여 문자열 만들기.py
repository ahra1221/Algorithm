def solution(my_strings, parts):
    answer = ''
    idx = 0
    for idx, st in enumerate(my_strings):
        s, e = parts[idx][0], parts[idx][1]
        answer += st[s:e+1]
    return answer