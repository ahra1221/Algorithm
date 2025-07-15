def solution(num_list):
    ev = ''
    od = ''
    for num in num_list:
        if not(num%2):
            ev += str(num)
        else:
            od += str(num)
    return int(ev) + int(od)