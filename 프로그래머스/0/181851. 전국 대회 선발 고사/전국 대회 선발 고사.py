def solution(rank, attendance):
    answer = 0
    win = []
    students = dict(zip(rank, attendance))
    for a, b in sorted(students.items(), key=lambda item: item[0]):
        if b:
            win.append(rank.index(a))
    answer = 10000 * win[0] + 100 * win[1] + win[2]
    return answer