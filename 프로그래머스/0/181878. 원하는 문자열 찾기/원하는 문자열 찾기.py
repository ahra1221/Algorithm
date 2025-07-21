def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    if myString.find(pat) > -1:
        return 1
    else:
        return 0