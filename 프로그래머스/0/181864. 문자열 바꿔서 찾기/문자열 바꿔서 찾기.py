def solution(myString, pat):
    tmp = ''
    for st in myString:
        if st == 'A':
            tmp += 'B'
        else:
            tmp += 'A'
    if tmp.find(pat) > -1:
        return 1
    else:
        return 0