import sys

input = sys.stdin.readline
students = [int(input().strip()) for _ in range(28)]
students.sort()
missing = sorted(set(range(1,31)) - set(students))
print(*missing, sep="\n")