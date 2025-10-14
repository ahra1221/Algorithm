import sys, re
from collections import defaultdict, Counter
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    score = 1
    d = defaultdict(list)
    race = list(map(int, input().split()))
    cnt = Counter(race)
    for r in race:
        if cnt[r] >= 6:
            d[r].append(score)
            score += 1
    score_sum = {k: sum(v[:4]) for k, v in d.items() if len(v) >= 6}
    minv = min(score_sum.values())
    candidates = {k: v for k, v in score_sum.items() if v == minv}
    ans = 0
    if len(set(candidates.values())) == 1:
        fives = {k: d[k][4] for k in candidates}
        ans = min(fives, key=fives.get)
    else:
        ans = min(candidates, key=candidates.get)

    print(ans)