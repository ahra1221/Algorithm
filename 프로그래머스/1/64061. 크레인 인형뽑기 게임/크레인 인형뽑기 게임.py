def pick(arr):
    for idx, a in enumerate(arr):
        if a > 0:
            return idx
    return -1
        
def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    lines = {}
    l = 1
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(board[j][i])
        lines[l] = tmp
        l += 1
    
    for m in moves:
        pick_idx = pick(lines[m])
        if pick_idx >= 0: #뽑을수있음
            basket.append(lines[m][pick_idx])
            lines[m][pick_idx] = 0
        else:
            continue
        while len(basket) >= 2 and basket[-1] == basket[-2]:
            basket = basket[:-2]
            answer += 2
    return answer