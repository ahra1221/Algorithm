def timeToDay(day):
    y, m, d = map(int, day.split('.'))
    return y * 12 * 28 + m * 28 + d


def solution(today, terms, privacies):
    answer = []
    term = {}
    today = timeToDay(today)

    for t in terms:
        x, y = t.split()
        term[x] = int(y)

    for idx, p in enumerate(privacies):
        start_day, kind = p.split()
        if timeToDay(start_day) + term[kind] * 28 <= today:
            answer.append(idx+1)
        
    return answer