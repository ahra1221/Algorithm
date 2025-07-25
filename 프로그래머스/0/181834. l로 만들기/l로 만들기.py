def solution(myString):
    answer = ''
    for st in myString:
        if st < 'l':
            answer += 'l'
        else:
            answer += st
    return answer