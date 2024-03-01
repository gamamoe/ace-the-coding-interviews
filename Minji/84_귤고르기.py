from collections import Counter

def solution(k, tangerine):
	cnt = Counter(tangerine)
	res, tot = 0, 0
  
	lists = sorted(cnt.values(), reverse=True)
  
	for count in lists:
			tot += count
			res += 1
  
			if tot >= k:
				break
  
	return res

assert solution( 6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3
assert solution( 4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2
assert solution( 2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1