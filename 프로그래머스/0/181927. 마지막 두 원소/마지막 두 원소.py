def solution(num_list):
    l = len(num_list) - 1
    a = num_list[l]
    b = num_list[l-1]
    if a>b:
        num_list.append(a-b)
    else:
        num_list.append(2*a)
    return num_list