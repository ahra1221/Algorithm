def solution(s):
    answer = []
    
    total = 0
    zero_count = 0
    while s != '1':
        zero_count += s.count('0')
        s = s.replace('0','')
        l = len(s)
        tmp = ""
        while l>0:
            tmp += str(l % 2)
            l //= 2
        s = tmp[::-1]
        total += 1
    answer.append(total)
    answer.append(zero_count)
    return answer