def solution(board):

  def is_valid(row_val, col_val, num):
    return not (in_row(num, row_val) or in_col(num, col_val) or in_box(num, row_val, col_val))
  
  def in_row(num, row_val):
    return num in board[row_val]
  
  def in_col(num, col_val):
    for i in range(len(board)):
      if board[i][col_val] == num:
        return True
    
    return False
  
  def in_box(num, row_val, col_val):
    start_row = row_val - row_val % 3
    start_col = col_val - col_val % 3
    
    for i in range(3):
      for j in range(3):
        if board[start_row + i][start_col + j] == num:
          return True
        
    return False
  
  def find_empty():
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == 0:
          return (i, j)
        
    return None
  
  empty_loc = find_empty()
  if not empty_loc:
    return board
  row, col = empty_loc
  
  for num in range(1, 10):
    if is_valid(row, col, num):
      board[row][col] = num
      if solution(board):
        return board
      board[row][col] = 0
      
  return False

assert solution([
	[5, 3, 0, 0, 7, 0, 0, 0, 0],
	[6, 0, 0, 1, 9, 5, 0, 0, 0],
	[0, 9, 8, 0, 0, 0, 0, 6, 0],
	[8, 0, 0, 0, 6, 0, 0, 0, 3],
	[4, 0, 0, 8, 0, 3, 0, 0, 1],
	[7, 0, 0, 0, 2, 0, 0, 0, 6],
	[0, 6, 0, 0, 0, 0, 2, 8, 0],
	[0, 0, 0, 4, 1, 9, 0, 0, 5],
	[0, 0, 0, 0, 8, 0, 0, 7, 9],
]) == [
	[5, 3, 4, 6, 7, 8, 9, 1, 2],
	[6, 7, 2, 1, 9, 5, 3, 4, 8],
	[1, 9, 8, 3, 4, 2, 5, 6, 7],
	[8, 5, 9, 7, 6, 1, 4, 2, 3],
	[4, 2, 6, 8, 5, 3, 7, 9, 1],
	[7, 1, 3, 9, 2, 4, 8, 5, 6],
	[9, 6, 1, 5, 3, 7, 2, 8, 4],
	[2, 8, 7, 4, 1, 9, 6, 3, 5],
	[3, 4, 5, 2, 8, 6, 1, 7, 9],
]