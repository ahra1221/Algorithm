import sys

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    
    if arr[0] == 0: break
    
    k = arr[0]
    nums = arr[1:]
    
    def dfs(st, cur):
        if len(cur) == 6:
            print(*cur)
            return
        
        for i in range(st, k):
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
    
    dfs(0, [])
    print()