T = int(input())
for _ in range(T):
    ps = input()
    st = []
    isVPS = True
    for i in ps:
        if i == "(":
            st.append(i)
        elif i == ")":
            if st:
                st.pop()
            else:
                isVPS = False
                break
    if not st and isVPS:
        print("YES")
    else:
        print("NO")
