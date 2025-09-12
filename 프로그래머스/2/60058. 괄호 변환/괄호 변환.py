def solution(p):
    if not p:
        return ""
    u,v = split_balance_str(p)
    if right_str(u):
        return u + solution(v)
    else: 
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        tmp += ''.join(')' if i == '(' else '(' for i in u[1:-1])
        return tmp

def right_str(check):
    st = []
    for s in check:
        if s == "(":
            st.append(s)
        else:
            if not st:
                return False
            st.pop()
    return not st

def split_balance_str(check):
    open_cnt = 0
    close_cnt = 0
    for idx, s in enumerate(check):
        if s == "(": open_cnt += 1
        else: close_cnt += 1
        if open_cnt == close_cnt:
            return (check[:idx+1], check[idx+1:])
