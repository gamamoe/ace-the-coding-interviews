def solution(s):
  x = 0
  s_len = len(s)
  
  for i in range(s_len):
    stack = []
    for j in range(s_len):
      c = s[(i + j) % s_len]
      
      if c == "{" or c == "[" or c == "(":
        stack.append(c)
      else:
        if not stack:
          break
        
        if c == ")" and stack[-1] == "(":
          stack.pop()
        elif c == "]" and stack[-1] == "[":
          stack.pop()
        elif c == "}" and stack[-1] == "{":
          stack.pop()
        else:
          break
        
    else:
      if not stack:
        x += 1
  
  return x
