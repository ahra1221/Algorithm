while True:
    str = input()
    if str == ".":
        break
    st = []
    for s in str:
        if (s == "(") or (s == "["):
            st.append(s)
        elif s == ")":
            if len(st) > 0 and st[-1] == "(":
                st.pop()
            else : 
                st.append(']')
                break
        elif s == "]":
            if len(st) > 0 and st[-1] == "[":
                st.pop()
            else:
                st.append(s)
                break
    print("yes" if len(st) == 0 else "no")