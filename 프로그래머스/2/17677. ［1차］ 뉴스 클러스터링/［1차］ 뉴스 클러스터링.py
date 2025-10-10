def ready_set(st):
    res = []
    for i in range(len(st)-1):
        tmp = st[i:i+2]
        if tmp.isalpha():
            res.append(tmp)
    return res

def intersec(aset,bset):
    res = []
    intersec = set(aset) & set(bset)
    for i in intersec:
        n = min(aset.count(i), bset.count(i))
        res += [i] * n
    return res

def union(aset,bset):
    res = []
    union = set(aset) | set(bset)
    for u in union:
        n = max(aset.count(u), bset.count(u))
        res += [u] * n
    return res

def solution(str1, str2):
    answer = 0
    A = len(intersec(ready_set(str1.lower()), ready_set(str2.lower())))
    B = len(union(ready_set(str1.lower()), ready_set(str2.lower())))
    if A == 0 and B == 0:
        answer = 65536
    else:
        answer = int((A/B) * 65536)
    return answer