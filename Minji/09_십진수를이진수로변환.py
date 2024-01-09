def solution(decimal):
  stack = []
  binary = ""
  
  while decimal > 0:    
    stack.append(str(decimal % 2))
    decimal //= 2
  
  while stack:
    binary += stack.pop()
    
  return binary


decimal = 10
solution(decimal)