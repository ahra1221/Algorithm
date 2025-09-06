import sys

input = sys.stdin.readline
keyboard = [
    # a b c d e f g
    (2,1),(3,5),(3,3),(2,3),(1,3),(2,4),(2,5),
    # h i j k l m n 
    (2,6),(1,8),(2,7),(2,8),(2,9),(3,7),(3,6),
    # o p q r s t u
    (1,9),(1,10),(1,1),(1,4),(2,2),(1,5),(1,7),
    # v w x y z
    (3,4),(1,2), (3,2),(1,6),(3,1)
]
left_keys = {'q','w','e','r','t','a','s','d','f','g','z','x','c','v'}

sl, sr = input().split()
goal = input().strip()
nl = keyboard[ord(sl)-97]
nr = keyboard[ord(sr)-97]
ans = 0

def cal_dis(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for g in goal:
    gp = keyboard[ord(g)-97]
    is_left = g in left_keys
    if is_left:
        ans += cal_dis(gp, nl)
        nl = gp
    else:
        ans += cal_dis(gp, nr)
        nr = gp
    ans += 1
    
print(ans)