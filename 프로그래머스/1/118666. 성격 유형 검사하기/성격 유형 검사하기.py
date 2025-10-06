from collections import defaultdict

def check_sim(le,ri,choice):
    if choice < 4:
        return (le, 4-choice)
    elif choice > 4:
        return (ri, choice-4)
    else:
        return None

def cal_res(score):
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    res = ""
    for a,b in pairs:
        if score[a] > score[b]:
            res += a
        elif score[a] < score[b]:
            res += b
        else:
            res += min(a, b) 
    return res
        

def solution(survey, choices):
    answer = ''
    score = defaultdict(int)
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for idx,s in enumerate(survey):
        res = check_sim(s[0],s[1],choices[idx])
        if res:
            score[res[0]] += res[1]
    for a,b in pairs:
        if score[a] > score[b]:
            answer += a
        elif score[a] < score[b]:
            answer += b
        else:
            answer += min(a, b) 
    return answer