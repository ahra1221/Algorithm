import sys

input = sys.stdin.readline
N,S = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

def dfs(st, total):
    global answer
    if st == N:
        if total == S:
            answer += 1
        return
    
    dfs(st+1, total + nums[st])
    dfs(st+1, total)
 
dfs(0,0)  
if S == 0: answer -= 1      
print(answer)