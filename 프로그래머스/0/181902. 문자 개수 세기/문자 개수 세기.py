def solution(my_string):
    answer = [0] * 52
    for st in my_string:
        tmp = ord(st)
        if st.islower():
            answer[tmp - 97 + 26] += 1
        else:
            answer[tmp - 65] += 1
    return answer