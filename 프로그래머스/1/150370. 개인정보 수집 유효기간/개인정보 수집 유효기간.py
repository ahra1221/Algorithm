def cal_expire(start, month):
    y,m,d = map(int, start.split("."))
    m += month
    d -= 1
    if d < 1:
        m -= 1
        d = 28
    if m > 12:
        y += (m-1) // 12
        m = 12 if m % 12 == 0 else m % 12
    elif m < 1:
        y -= 1
        m = 12
    return f"{y}.{m:02}.{d:02}"

def is_expire(today, ex):
    return tuple(map(int, today.split("."))) > tuple(map(int, ex.split(".")))

def solution(today, terms, privacies):
    answer = []
    term = {k: int(v) for k, v in (t.split() for t in terms)}
    for idx, pri in enumerate(privacies):
        d, k = pri.split()
        if is_expire(today, cal_expire(d, term[k])):
            answer.append(idx+1)
    return answer