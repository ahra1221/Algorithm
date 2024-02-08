def is_hansu(n):
    result = 0
    for i in range(1, n + 1):
        string_num = list(map(int, str(i)))
        if i < 100:
            result += 1
        elif string_num[1] - string_num[0] == string_num[2] - string_num[1]:
            result += 1
    return result


num = int(input())
print(is_hansu(num))