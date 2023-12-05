def solution(s):
    st = []

    for i in s:  # 마지막에 있는게 현재 문자와 같으면 pop
        if st and st[-1] == i:
            st.pop()
        else:  # 나머진 append
            st.append(i)

    if st:  # stack이 남아있으면
        return 0
    else:  # stack이 비어있으면
        return 1