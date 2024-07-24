def solution(s):
    s = s.lower()
    p_cnt = s.count('p')
    y_cnt = s.count('y')
    return p_cnt == y_cnt