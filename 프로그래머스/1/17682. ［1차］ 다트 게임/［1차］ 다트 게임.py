import re

def solution(dartResult):
    answer = 0
    process = []
    darts = re.findall(r'\d+\D+', dartResult)
    for dart in darts:
        score = int(re.match(r'\d+', dart).group())
        bonus = re.search(r'[SDT]', dart).group()
        if bonus == "D":
            score = pow(score,2)
        elif bonus == "T":
            score = pow(score,3)
        
        option = re.search(r'[*#]', dart)
        if option:
            op = option.group()
            if op == "#":
                score *= -1
            else:
                score *= 2
                if process:
                    process.append(process.pop() * 2)
        process.append(score)
                
    return sum(process)