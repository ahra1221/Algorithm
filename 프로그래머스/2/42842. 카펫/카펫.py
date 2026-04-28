import math
def solution(brown, yellow):
    answer = []
    candidate = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            candidate.append((yellow // i,i))
    
    candidate.sort()
    for r,c in candidate:
        b = 2*r + 2*c + 4
        if b == brown:
            answer = [r+2,c+2]
            break
    return answer