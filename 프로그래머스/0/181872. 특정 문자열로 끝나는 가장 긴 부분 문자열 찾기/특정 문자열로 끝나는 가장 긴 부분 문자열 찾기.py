def solution(myString, pat):
    answer = ''
    idx = myString.rfind(pat)
    answer = myString[:idx + len(pat)]
    return answer