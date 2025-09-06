import sys

input = sys.stdin.readline

while True:
    try:
        s, t = input().split()
        idx = 0
        ans = False
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    ans = True
                    break
        print("Yes" if ans else "No")
    except:
        break