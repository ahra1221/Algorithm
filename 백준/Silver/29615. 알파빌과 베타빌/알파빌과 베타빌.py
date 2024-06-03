N, M = map(int, input().split())
city_list = input().split()
friend_num = input().split()

result = 0
for c in city_list[:M]:
    if c not in friend_num:
        result += 1
        
print(result)