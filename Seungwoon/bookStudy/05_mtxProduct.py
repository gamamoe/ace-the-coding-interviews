def solution(arr1, arr2):
    arr1_row = len(arr1)
    arr1_col = len(arr1[0])
    arr2_col = len(arr2[0])
    answer = [[0] * arr2_col for _ in range(arr1_row)]
    for i in range(arr1_row):
        for j in range(arr2_col):
            for k in range(arr1_col):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer
'''
<메모>
행렬 정의할 때, 
r1, c1 = 
r2, c2 = 
이런식으로 깔끔하게 정의하자.
-> 행1 열1 행2 열2 일때, 열1과 행2의 숫자가 같고 행1과 열2가 행렬의 크기가 된다.
2차원 배열에서 for문(r1)은 행을 형성.  단순 곱(c2)는 열을 형성
'''
