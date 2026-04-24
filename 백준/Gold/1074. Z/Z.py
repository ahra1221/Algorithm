import sys

input = sys.stdin.readline
N,r,c = map(int, input().split())
answer = 0

def visit(x,y,size):
    global answer
    
    if size == 1: return
    
    half = size // 2
    area = half * half
    
    if r < x + half and c < y + half: #1사분면
        visit(x,y,half)
    
    elif r < x + half and c >= y + half: #2사분면
        answer += area
        visit(x,y+half,half)
                
    elif r >= x + half and c < y + half: #3사분면
        answer += area * 2
        visit(x+half,y,half)
    
    elif r >= x + half and c >= y + half: #4사분면
        answer += area * 3
        visit(x+half,y+half,half)

visit(0,0,2 ** N)
print(answer)