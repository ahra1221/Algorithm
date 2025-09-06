import sys

input = sys.stdin.readline
vo = ['a','e','i','o','u']

def check_pw(pw):
    #1
    hasv = False
    for v in vo:
        if v in pw:
            hasv = True
            break
    if not hasv:
        return False
    #2
    v = 0
    nv = 0
    for p in pw:
        if p in vo:
            nv = 0
            v += 1
        else:
            v = 0
            nv += 1
        if v == 3 or nv == 3:
            return False
    #3
    for idx in range(1, len(pw)):
        if pw[idx]=='e' or pw[idx]=='o':
            continue
        if pw[idx-1] == pw[idx]:
            return False
    return True

while True:
    st = input().strip()
    if st == 'end':
        break
    else:
        ans = check_pw(st)
        if ans:
            print("<%s> is acceptable."%st)
        else:
            print("<%s> is not acceptable."%st)