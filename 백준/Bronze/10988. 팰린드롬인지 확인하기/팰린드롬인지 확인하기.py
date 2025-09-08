import sys

input = sys.stdin.readline
string = input().strip()
ans = True
end = len(string)//2 if not len(string)/2 else len(string)//2 -1

for i in range(end+1):
    if string[i] != string[len(string)-i-1]:
        ans = False
        break

print(int(ans))