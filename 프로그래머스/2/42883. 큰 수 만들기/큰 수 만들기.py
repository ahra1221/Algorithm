def solution(number, k):
    answer = ''
    num = []
    for i in number:
        if not num:
            num.append(i)
            continue
        if k > 0:
            while num[-1] < i:
                num.pop()
                k -= 1
                if not num or k <= 0:
                    break
        num.append(i)
    num = num[:-k] if k > 0 else num
    return ''.join(num)