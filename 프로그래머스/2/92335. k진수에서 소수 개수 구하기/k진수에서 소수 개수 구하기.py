def to_base_n(n, num):
    digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    res = []
    while num > 0:
        res.append(digits[num % n])
        num //= n
    return ''.join(reversed(res))  

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def solution(n, k):
    answer = 0
    target = to_base_n(k, n)
    sp = target.split("0")
    for s in sp:
        if s == '':
            continue
        if is_prime(int(s)):
            answer += 1
    return answer
