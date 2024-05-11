import sys

input = sys.stdin.readline

while True:
    num = input().strip()
    if num == '0':
        break
    else:
        reverse_num = num[::-1]
        if reverse_num == num:
            print("yes")
        else:
            print("no")

