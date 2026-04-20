def solution(s, n):
    answer = ''
    for str in s:
        if str.isupper():
            tmp = (ord(str) - ord('A') + n) % 26
            answer += chr(tmp + 65)
        elif str.islower():
            tmp = (ord(str) - ord('a') + n) % 26
            answer += chr(tmp + 97)
        else:
            answer += str
    return answer