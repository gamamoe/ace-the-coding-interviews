def solution(n):
  lists = list(map(int, str(n)))
  
  lists.sort(reverse=True)
  
  res = int(''.join(map(str, lists)))
  
  return res

assert solution(118372) == 873211