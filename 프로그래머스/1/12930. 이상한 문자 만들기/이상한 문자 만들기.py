def solution(s):
    changes = []
    for word in s.split(" "):
        tmp = ""
        for idx, w in enumerate(word):
            if idx % 2 == 0:
                tmp += w.upper()
            else:
                tmp += w.lower()
        changes.append(tmp)
    
    answer = " ".join(changes)
    return answer