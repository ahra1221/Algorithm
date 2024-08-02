def solution(s):
    answer = ''
    low_str = []
    up_str = []
    for str in s:
        if str.isupper():
            up_str.append(str)
        else:
            low_str.append(str)
    low_str.sort(reverse=True)
    up_str.sort(reverse=True)
    answer += "".join(low_str)
    answer += "".join(up_str)
    return answer