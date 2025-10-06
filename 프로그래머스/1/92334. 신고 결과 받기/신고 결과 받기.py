from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    complain = defaultdict(int)
    id_per_complain = defaultdict(list)
    for r in set(report):
        a,b = r.split()
        complain[b] += 1
        id_per_complain[a].append(b)
    complain = set(key for key,val in complain.items() if val >= int(k))
    for id in id_list:
        tmp = complain & set(id_per_complain[id])
        answer.append(len(tmp))
    return answer