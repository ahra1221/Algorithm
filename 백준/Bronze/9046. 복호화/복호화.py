import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    string = input().strip()
    dict = {}
    for s in string:
        if s == ' ':
            continue
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    best = max(dict.values())
    best_key = [k for k, v in dict.items() if v == best]
    if len(best_key) > 1:
        print("?")
    else:
        print(max(dict, key=dict.get))
