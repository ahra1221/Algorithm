import sys
import re

input = sys.stdin.readline
N = int(input())
pattern = re.compile('^[ABCDEF]?A+F+C+[ABCDEF]?$')

for _ in range(N):
    n = input().strip()
    if pattern.match(n) == None:
        print("Good")
    else:
        print("Infected!")