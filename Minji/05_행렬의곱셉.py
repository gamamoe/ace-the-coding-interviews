def solution(arr1, arr2):
  # 2차원 행렬 arr1과 arr2를 입력 받아 arr1에 arr2를 곱한 결과를 반환하는 함수 완성
  result = [[0 for j in range(len(arr2))] for i in range(len(arr1))]
  
  for i in range(len(arr1)):
    for j in range(len(arr1[i])):
      for k in range(len(arr2)):
        print("=== i : ", i, ", j : ", j, ", k : ", k)
        result[i][j] += arr1[i][k] * arr2[k][j]
        print("==== result: ", result[i][j], ", list : ", result)
  
  return result


arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
# result = [[15, 15],[15, 15],[15, 15]]
solution(arr1, arr2)

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# result = [[22, 22, 11],[36, 28, 18],[29, 20, 14]]
solution(arr1, arr2)