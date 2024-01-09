def solution(arr):
	for i in range(0, len(arr)):
		if(arr.count(i) > 1):
			arr.pop(i)

	arr.sort(reverse=True)
	# print(arr)
	return 

arr = [4, 2, 2, 1, 3, 4]
solution(arr)