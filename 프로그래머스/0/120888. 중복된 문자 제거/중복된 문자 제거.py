def solution(my_string):
    answer = ''
    str_set = set()
    for s in my_string:
        if s not in str_set:
            answer += s
            str_set.add(s)
    return answer