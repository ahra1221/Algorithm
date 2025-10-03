from collections import defaultdict

def solution(friends, gifts):
    giftnum = defaultdict(int)
    total = defaultdict(lambda: defaultdict(int))
    
    for g in gifts:
        give, receive = map(str, g.split())
        total[give][receive] += 1
        giftnum[give] += 1
        giftnum[receive] -= 1
        
    received = {name: 0 for name in friends}
    n = len(friends)
    for i in range(n):
        for j in range(i+1, n):
            a,b = friends[i],friends[j]
            atob = total.get(a, {}).get(b, 0)
            btoa = total.get(b, {}).get(a, 0)
            
            if atob > btoa: #준게 더 많음
                received[a] += 1
            elif atob < btoa:
                received[b] += 1
            else: #같으면선물지수로
                if giftnum[a] > giftnum[b]:
                    received[a] += 1
                elif giftnum[b] > giftnum[a]:
                    received[b] += 1
    return max(received.values()) if received else 0

