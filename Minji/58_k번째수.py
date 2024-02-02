def solution(ary, commands):
  res = []
  
  for c in commands:
    i, j, k = c
    
    sort_ary = sorted(ary[i-1:j])
    
    res.append(sort_ary[k-1])
  
  return res

assert solution(
  [1, 5 ,2, 6, 3, 7, 4], 
  [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]