from collections import Counter, defaultdict
def solution(N, stages):
    answer = []
    failure = {}
    total = len(stages)
    d = defaultdict(int, Counter(stages))

    for i in range(1, N+1):
        if total == 0:
            failure[i] = 0
        else:
            failure[i] = d[i] / total
            total -= d[i]
    answer = [k for k, v in sorted(failure.items(), key=lambda x:(-x[1],x[0]))]
        
    return answer