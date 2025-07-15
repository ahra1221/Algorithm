def solution(code):
    answer = ''
    mode = False
    for idx in range(len(code)):
        st = code[idx]
        if st != "1":
            if not mode and not(idx % 2):
                answer += st
            elif mode and (idx % 2) > 0 :
                answer += st
        else:
            mode = not mode
    if not answer:
        answer = "EMPTY"
    return answer