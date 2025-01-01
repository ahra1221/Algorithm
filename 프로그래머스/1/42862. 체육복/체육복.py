def solution(n, lost, reserve):
    answer = n
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for j in set_reserve:
        if (j-1) in set_lost:
            set_lost.remove(j-1)
        elif (j+1) in set_lost:
            set_lost.remove(j+1)
    return n - len(set_lost)