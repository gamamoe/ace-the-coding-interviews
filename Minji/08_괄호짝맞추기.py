def solution(s):
  stack = []
  
  for i in s:
    if i == "(":
      stack.append(i)
    elif i == ")":
      if len(stack) == 0:
        return False
      else:
        stack.pop()
        
  if len(stack) == 0:
    return True
  else:
    return False


  
s = "(())()"
solution(s)

s = "((())()"
solution(s)