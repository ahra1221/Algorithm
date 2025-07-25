def solution(str_list, ex):
    answer = ''
    for st in str_list:
        if ex not in st:
            answer += st
    return answer