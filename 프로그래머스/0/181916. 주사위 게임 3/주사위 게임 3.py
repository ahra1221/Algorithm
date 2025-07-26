def solution(a, b, c, d):
    answer = 0
    nums = [a,b,c,d]
    cnt = [nums.count(x) for x in nums]
    print(cnt)
    if max(cnt) == 4:
        answer = 1111 * a
    elif max(cnt) == 3:
        answer = (10 * nums[cnt.index(3)] + nums[cnt.index(1)]) ** 2
    elif max(cnt) == 1:
        answer = min(nums)
    else:
        if min(cnt) == 1:
            tmp = 1
            for idx, c in enumerate(cnt):
                if c == 1:
                    tmp *= nums[idx]
            answer = tmp
        else:
            uniq = list(set(nums))
            p = uniq[0]
            q = uniq[1]
            answer = (p + q) * abs(p - q)
    return answer