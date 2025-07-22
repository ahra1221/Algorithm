def solution(myString):
    answer = [st for st in myString.split('x') if st]
    return sorted(answer)