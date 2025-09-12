import sys
import math

input = sys.stdin.readline
h,w,n,m = map(int, input().split()) 
ans = math.ceil((h / (n+1))) * math.ceil((w / (m+1)))
print(int(ans))