num = int(input())
number_list = set(map(int, input().split()))

num2 = int(input())
number_list2 = list(map(int, input().split()))

for _ in number_list2:
    if _ in number_list:
        print("1")
    else:
        print("0")