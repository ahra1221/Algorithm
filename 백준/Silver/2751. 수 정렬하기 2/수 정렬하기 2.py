num = int(input())
number_list: [int] = []

for i in range(num):
    number_list.append(int(input()))

for j in sorted(number_list):
    print(j)