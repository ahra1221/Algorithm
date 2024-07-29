def solution(s):
    answer = True
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if not st:
                return False
            else:
                st.pop() 
    return not st