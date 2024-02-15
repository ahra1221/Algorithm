n = input()
n = sorted(n, reverse=True)
result = 0

if "0" not in n:
    print(-1)
else:
    for i in n:
        result += int(i)
    if result % 3 != 0:
        print(-1)
    else:
        print(''.join(n))