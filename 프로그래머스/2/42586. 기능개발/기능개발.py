import math

def solution(progresses, speeds):
    answer = []
    works = [math.ceil((100 -progresses[i]) / speeds[i]) for i in range(len(speeds))]
    cnt = 0
    for i in range(len(works)):
        if works[cnt] < works[i]:
            answer.append(i - cnt)
            cnt = i
    answer.append(len(works) - cnt)
    return answer