def solution(myString, pat):
    answer = 0
    for i in range(0, len(myString)):
        tmp = myString[i: i + len(pat)]
        if tmp == pat:
            answer += 1
    return answer