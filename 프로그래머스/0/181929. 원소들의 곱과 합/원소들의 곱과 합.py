def solution(num_list):
    answer = 0
    mul = 1
    sum = 0
    for num in num_list:
        mul *= num
        sum += num
    sum *= sum
    return 1 if mul < sum else 0