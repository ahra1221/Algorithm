import sys
input = sys.stdin.readline
n,game = map(str, input().split())
num = {"Y": 2, "F": 3, "O": 4}
plays = set()

for _ in range(int(n)):
    player = input().strip()
    plays.add(player)

ans = len(plays) // (num[game]-1)
print(ans)