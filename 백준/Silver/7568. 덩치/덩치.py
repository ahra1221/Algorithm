num = int(input())
student_info = []

for i in range(num):
    weight, height = map(int, input().split())
    student_info.append((weight, height))

for j in student_info:
    rank = 1
    for k in student_info:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end=" ")