def solution(answers):
  result = []
  pattern = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	]
  count1 = count2 = count3 = 0
  
  for i in range(len(pattern)):
    for j in range(len(answers)):
      if(pattern[i][j] == answers[j]):
        if(i == 0):
          count1 += 1
        elif(i == 1):
          count2 += 1
        else:
          count3 += 1

  cnt = [count1, count2, count3]
  max_cnt = max(cnt)
  
  for i in range(len(cnt)):
    if max_cnt == cnt[i]:
      result.append(i + 1)
  
  # print(result)
  return sorted(result)


answers = [1, 2, 3, 4, 5]
solution(answers)

answers2 = [1, 3, 2, 4, 2]
solution(answers2)