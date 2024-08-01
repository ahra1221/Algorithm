def solution(n):
    answer = ""
    arr = [i for i in str(n)]
    arr.sort(reverse=True)
    for j in arr:
        answer += j
    return int(answer)