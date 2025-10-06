def cal_dis(st, en):
    return abs(st[0]-en[0]) + abs(st[1]-en[1])

def solution(numbers, hand):
    answer = ''
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    leftpad = {1,4,7}
    rightpad = {3,6,9}
    lp = pos['*']
    rp = pos['#']
    
    for num in numbers:
        if num in leftpad:
            used = 'L'
        elif num in rightpad:
            used = 'R'
        else:
            froml = cal_dis(lp,pos[num])
            fromr = cal_dis(rp,pos[num])
            if froml < fromr:
                used = 'L'
            elif froml > fromr:
                used = 'R'
            else:
                if hand == "right":
                    used = 'R'
                else:
                     used = 'L'
        if used == 'L':
            lp = pos[num]
        else:
            rp = pos[num]
        answer += used
        
    return answer