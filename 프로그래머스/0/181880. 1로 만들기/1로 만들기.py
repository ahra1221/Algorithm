def solution(num_list):
    answer = 0
    for num in num_list:
        while num > 1:
            if not num % 2:
                num /= 2
            else:
                num = (num -1) / 2
            answer += 1
    return answer 