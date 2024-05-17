import sys

input = sys.stdin.readline

n, m = map(int, input().split())
string = [input().strip() for _ in range(n)]

milk_dict = {'.': '.', 'O': 'O', '-': '|', '|': '-', '/': "\\", "\\": '/',
             '^': '<', '<': 'v', 'v': '>', '>': '^'}

for i in range(m-1, -1, -1):
    for j in range(n):
        print(milk_dict.get(string[j][i]), end='')
    print()
    