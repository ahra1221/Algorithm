s = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
ans = 0

i = 0
while i < len(s):
    if s[i:i+3] in cro:
        i += 3
    elif s[i:i+2] in cro:
        i += 2
    else:
        i += 1 
    ans += 1

print(ans)