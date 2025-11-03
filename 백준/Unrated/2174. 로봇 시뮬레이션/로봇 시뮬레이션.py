import sys

input = sys.stdin.readline
a,b = map(int, input().split())
n,m = map(int, input().split())
robot_pos = []
robot_dir = []
dircan = ["N","E","S","W"]
dirs = {
    "N": (0,1),
    "E": (1,0),
    "S": (0,-1),
    "W": (-1,0)
    }
for _ in range(n):
    x,y,d = map(str, input().split())
    robot_pos.append([int(x), int(y)])
    robot_dir.append(d)
for _ in range(m):
    r,com,num = map(str, input().split())
    r = int(r)
    num = int(num)
    if com == "F":
        nx,ny = robot_pos[r-1]
        dx,dy = dirs[robot_dir[r-1]]
        for i in range(num):
            nx += dx
            ny += dy
            if not(1<=nx<=a and 1<=ny<=b):
                print(f"Robot {r} crashes into the wall")
                sys.exit(0)
            for i in range(n):
                if i != r-1 and robot_pos[i][0] == nx and robot_pos[i][1] == ny:
                    print(f"Robot {r} crashes into robot {i+1}")
                    sys.exit(0)
        robot_pos[r-1] = [nx, ny]
    elif com == "L":
        robot_dir[r-1] = dircan[(dircan.index(robot_dir[r-1]) - num) % 4]
    elif com == "R":
        robot_dir[r-1] = dircan[(dircan.index(robot_dir[r-1]) + num) % 4]

print("OK")
