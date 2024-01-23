def solution(n):
  res = []
  
  def bt(n, start, tot, cur_sum, cur, res):
    if cur_sum == tot:
      res.append(cur.copy())
      return res
    
    for i in range(start, n+1):
      if cur_sum + i <= tot:
        cur.append(i)
        cur_sum += i
        
        bt(n, i+1, tot, cur_sum, cur, res)
        
        cur.pop()
        cur_sum -= i
      
  bt(n, 1, 10, 0, [], res)
  
  return res

assert solution(5) == [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
assert solution(2) == []
assert solution(7) == [[1, 2, 3, 4], [1, 2, 7], [1, 3, 6], [1, 4, 5],[2, 3, 5], [3, 7], [4, 6]]