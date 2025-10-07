def solution(number, k):
    answer = ''
    st = []
    cnt = 0
    for n in number:
        if cnt == k:
            st.append(n)
            continue
        while st and st[-1] < n:
            st.pop()
            cnt += 1
            if cnt == k:
                break
        st.append(n)
    if cnt < k:
        st = st[:-(k - cnt)]
    return "".join(st)