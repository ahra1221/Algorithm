import sys

input = sys.stdin.readline

while True:
    tri = sorted(list(map(int, input().split())))
    s = set(tri)
    if tri[0] == 0: break
    if tri[2] >= tri[1] + tri[0]:
        print("Invalid")
    else:
        l = len(s)
        if l == 1:
            print("Equilateral")
        elif l == 2:
            print("Isosceles")
        else:
            print("Scalene")
    