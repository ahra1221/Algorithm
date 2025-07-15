def solution(numLog):
    answer = ''
    key = dict(zip([1,-1,10,-10],["w","s","d","a"]))
    for i in range(1, len(numLog)):
        answer += key[numLog[i] - numLog[i-1]]
    return answer