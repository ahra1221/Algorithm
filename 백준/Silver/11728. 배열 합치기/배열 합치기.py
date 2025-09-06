import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = []
i, j = 0, 0

while i<N or j<M:
    if i>=N or (j<M and A[i]>B[j]):
        ans.append(B[j])
        j += 1
    else:
        ans.append(A[i])
        i += 1
print(" ".join(map(str, ans)))