def solution(strArr):
    answer = []
    for st in strArr:
        idx = st.find('ad')
        if idx == -1:
            answer.append(st)
    return answer