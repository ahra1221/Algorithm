def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2+1):
        print(i)
        zip_str = ""
        prev = ""
        cnt = 1
        for j in range(0,len(s),i):
            tmp = s[j:j+i]
            if prev == tmp:
                cnt += 1
            else:
                if cnt > 1:
                    zip_str += str(cnt) + prev
                    cnt = 1
                else:
                    zip_str += prev
                prev = tmp
        if cnt > 1:
            zip_str += str(cnt) + prev
            cnt = 1
        else:
            zip_str += prev
        answer = min(answer, len(zip_str))
    return answer