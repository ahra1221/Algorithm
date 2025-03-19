N = int(input())
nums = list(map(int, input().split()))
sort_nums = sorted(list(set(nums)))

dict = {value: idx for idx, value in enumerate(sort_nums)}

ans = []
for i in nums:
    ans.append(dict[i])
print(" ".join(map(str, ans)))