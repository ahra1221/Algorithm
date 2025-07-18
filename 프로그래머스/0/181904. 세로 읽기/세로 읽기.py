def solution(my_string, m, c):
    answer = ''
    for i in range(c, len(my_string)+1, m):
        answer += my_string[i-1]
    return answer