def solution(number):
    s = 0
    for n in number:
        s += int(n)
    return s % 9