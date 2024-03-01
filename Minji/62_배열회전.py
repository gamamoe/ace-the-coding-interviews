def solution(arr, n):
  k = len(arr)
  n = n % 4
  
  for _ in range(n):
    res = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(k):
      for j in range(k):
        res[j][k - 1 - i] = arr[i][j]
        
    arr = res
  # print(arr)
  return arr

assert solution(
	[
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]
	], 1
) == [
	[13, 9, 5, 1],
	[14, 10, 6, 2],
	[15, 11, 7, 3],
	[16, 12, 8, 4]
]

assert solution(
	[
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]
	], 2
) == [
	[16, 15, 14, 13],
	[12, 11, 10, 9],
	[8, 7, 6, 5],
	[4, 3, 2, 1]
]