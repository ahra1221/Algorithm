def solution(my_string, queries):
    answer = ''
    for st, en in queries:
        rev = ''.join(reversed(my_string[st:en+1]))
        my_string = my_string[0:st] + rev + my_string[en+1:]
    return my_string