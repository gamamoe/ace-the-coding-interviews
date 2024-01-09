def solution(string_list, query_list):
  lists = []
  res = []
  
  for i in range(len(string_list)):
    lists.append(string_list[i])
    
  for j in range(len(query_list)):
    if query_list[j] in lists:
      res.append(True)
    else:
      res.append(False)
      
  return res

string_list = ["apple", "banana", "cherry"]
query_list = ["banana", "kiwi", "melon", "apple"]
solution(string_list, query_list) # [True, False, False, True]