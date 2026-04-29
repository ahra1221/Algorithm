from itertools import permutations
def solution(expression):
    answer = 0
    operations = {'+', '-', '*'}
    
    tokens = []
    ops = set()
    prev = ""
    for exp in expression:
        if exp in operations:
            tokens.append(prev)
            prev = ""
            ops.add(exp)
            tokens.append(exp)
        else:
            prev += exp
    tokens.append(prev)
    
    for comb in permutations(list(ops), len(ops)):
        temp = tokens[:]
        for c in comb:
            st = []
            idx = 0
            while idx < len(temp):
                if temp[idx] == c:
                    prev = int(st.pop())
                    cur = int(temp[idx+1])
                    
                    if c == "*": st.append(prev * cur)
                    elif c == "+": st.append(prev + cur)
                    else: st.append(prev - cur)
                    idx += 2
                else:
                    st.append(temp[idx])
                    idx += 1
            temp = st
        answer = max(answer, abs(st[0]))
    
    return answer