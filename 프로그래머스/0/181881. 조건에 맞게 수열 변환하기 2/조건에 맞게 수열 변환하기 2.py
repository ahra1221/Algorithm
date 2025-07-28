def solution(arr):
    answer = 0
    old = arr
    while True:
        new = []
        for i in old:
            if i % 2 and i < 50:
                i = i * 2 + 1
            elif not(i % 2) and i >= 50:
                i /= 2
            new.append(int(i))
        if old == new:
            return answer 
        else:
            old = new
            answer += 1  
    return answer