def solution(num_list):
    answer = 0
    ev = sum(num_list[1::2])
    od = sum(num_list[::2])
    return ev if ev > od else od