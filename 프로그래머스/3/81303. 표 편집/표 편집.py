from collections import deque
def solution(n, k, cmd):    
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    next[-1] = -1
    
    delete = []
    answer = ["O"] * n
    
    for c in cmd:
        tmp = c.split(" ")
        com = tmp[0]
        if com == "U":
            x = int(tmp[1])
            for _ in range(x):
                k = prev[k]
        elif com == "D":
            x = int(tmp[1])
            for _ in range(x):
                k = next[k]
        elif com == "C":
            delete.append(k)
            answer[k] = "X"
            
            if prev[k] != -1:
                next[prev[k]] = next[k]
            
            if next[k] != -1:
                prev[next[k]] = prev[k]
            
            if next[k] != -1:
                k = next[k]
            else:
                k = prev[k]
                
        elif com == "Z":
            re = delete.pop()
            answer[re] = "O"
            
            if prev[re] != -1:
                next[prev[re]] = re
            
            if next[re] != -1:
                prev[next[re]] = re
    return "".join(answer)