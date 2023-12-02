def solution(numbers):
  result = []
  
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if(i != j):
        result.append(numbers[i] + numbers[j])
        result = sorted(set(result))
      
  # print(result)
  return result


numbers = [2,1,3,4,1]
solution(numbers)

numbers2 = [5,0,2,7]
solution(numbers2)