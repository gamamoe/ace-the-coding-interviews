#소괄호가 정상적으로 열고 닫혔는지 판별하는 함수 만들기
#idea: 가장 가까운.. 이라는 개념에서 스택 떠올리기
#하나의 통에 괄호 하나씩 입력하다가 닫는 괄호 나오면 같이 pop
def solution1(s):
    st = [] # stack을 담는 통
    for i in s:
        if i == '(':
            st.append(i)
        elif i == ')':
            if not st: # )가 나왔는데 기존이 비어있으면
                return False # early return
            else:
                st.pop() # )을 굳이 안넣고 기존 (만 pop
    if st: # 길이가 0이 아니면
        return False
    else:  # 길이가 0이면
        return True

s1 = '(())()' # Ture
s2 = '((())()' # False
s3 = ')(' # False
print(solution1(s1))
print(solution1(s2))
print(solution1(s3))