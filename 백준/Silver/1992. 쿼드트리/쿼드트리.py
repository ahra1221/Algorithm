import sys

input = sys.stdin.readline
N = int(input())
video = [list(map(int, input().strip())) for _ in range(N)]

def quadtree(x,y,size):
    first = video[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if video[i][j] != first:
                print("(", end="")
                #분할
                mid = size // 2
                quadtree(x,y,mid)
                quadtree(x,y+mid,mid)
                quadtree(x+mid,y,mid)
                quadtree(x+mid,y+mid,mid)
                print(")", end="")
                return
    print(first, end="")
                
quadtree(0,0,N)