import sys, re
input = sys.stdin.readline

m = int(input())
cookie = []
heart = (0,0)
ans = []

for i in range(m):
    l = input().strip()
    cookie.append(l)
    if re.search(r'\*{3,}',l):
        head = cookie[i-1].find("*")
        heart = (i, head)

arm = 0
for i in range(m): 
    if i == heart[1]:
        ans.append(arm)
        arm = 0
    elif cookie[heart[0]][i] == "*":
        arm += 1
ans.append(arm)

body = 0
body_end = 0
for i in range(heart[0]+1, m):
    if cookie[i][heart[1]] == "*":
        body += 1
    else:
        body_end = i
        break
ans.append(body)

left_leg = 0
for i in range(body_end, m):
    if cookie[i][heart[1]-1] == "*":
        left_leg += 1
    else:
        break
ans.append(left_leg)

right_leg = 0
for i in range(body_end, m):
    if cookie[i][heart[1]+1] == "*":
        right_leg += 1
    else:
        break
ans.append(right_leg)

print(heart[0]+1, heart[1]+1)
print(" ".join(map(str, ans)))