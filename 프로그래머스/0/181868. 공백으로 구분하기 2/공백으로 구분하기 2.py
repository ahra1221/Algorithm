def solution(my_string):
    answer = my_string.split(' ')
    answer = [i for i in answer if i != '']
    return answer