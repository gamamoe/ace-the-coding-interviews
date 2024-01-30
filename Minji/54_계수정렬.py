def solution(s):
  count = [0] * 26
  res = ""
  
  for i in s:
    count[ord(i) - ord('a')] += 1
    
  for i in range(len(count)):
    if count[i] > 0:
      for j in range(count[i]):
        alp = i + ord('a')
        res += chr(alp)
  
  return res

assert solution("hello") == "ehllo"
assert solution("algorithm") == "aghilmort"