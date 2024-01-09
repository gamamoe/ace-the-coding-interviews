def solution(N, stages):
  result = []
  res = {}
  challengers = len(stages)
  
  for i in range(1, N + 1):
    fails = stages.count(i)
    res[i] = fails / challengers
    challengers -= fails
  
  result = sorted(res, key=lambda x : res[x], reverse=True)
  
  print("==== result : ", result)
  return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# [3, 4, 2, 1, 5]
solution(N, stages)

N = 4
stages = [4, 4, 4, 4, 4]
# [4, 1, 2, 3]
solution(N, stages)