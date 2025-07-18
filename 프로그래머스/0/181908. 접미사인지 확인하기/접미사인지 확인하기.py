def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)):
        if is_suffix == my_string[i:]:
            return 1
    return answer