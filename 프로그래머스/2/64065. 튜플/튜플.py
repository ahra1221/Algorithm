import re

def solution(s):
    answer = []
    matches = re.findall(r'\{(.*?)\}', s[1:-1])
    match_list = [set(map(int, m.split(','))) for m in matches]
    match_list = sorted(match_list, key=len)
    for i in range(len(match_list)):
        if i > 0:
            value = next(iter(match_list[i] - match_list[i-1]))
        else:
            value = next(iter(match_list[i]))
        answer.append(value)
    return answer