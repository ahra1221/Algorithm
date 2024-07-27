def solution(clothes):
    answer = 1
    closet = {}
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]
            
    for _, value in closet.items():
        answer *= (len(value) + 1)
        
    return (answer - 1)