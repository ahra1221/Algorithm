def solution(s):
    answer = ''
    dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    tmp = ''
    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            tmp += i
            if tmp in dict:
                answer += str(dict[tmp])
                tmp = ''
    
    return int(answer)