N = int(input())
dots = []

for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort(key=lambda x: (x[1],x [0]))

for i in range(N):
    print(str(dots[i][0]) + " " + str(dots[i][1]))