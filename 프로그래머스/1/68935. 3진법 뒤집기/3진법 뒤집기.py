def solution(n):
    answer = 0
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    for i in range(len(s)):
        answer += int(s[len(s)-i-1]) * (3 ** i)
    return answer