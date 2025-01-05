t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    ans = 1
    for _ in range(n):
        _, i = input().split()
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict.values():
        ans *= (i+1)
    ans -=1
    print(ans)