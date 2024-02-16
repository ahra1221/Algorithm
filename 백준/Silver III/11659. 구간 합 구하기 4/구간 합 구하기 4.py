n, m = map(int, input().split())
arr = [0]
arr += list(map(int, input().split()))

for i, num in enumerate(arr):
    if i > 0:
        arr[i] = arr[i-1] + num

for _ in range(m):
    i , j = map(int, input().split())
    print(arr[j] - arr[i-1])