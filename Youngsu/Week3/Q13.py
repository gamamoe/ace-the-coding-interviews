def solution(board, moves):
    size = len(board)
    stack = []
    pung = 0
    for col in moves:
        row = 0
        while (board[row][col-1] == 0) and (row < size - 1):
            row += 1
        if board[row][col-1] != 0:
            if stack:
                if stack[-1] != board[row][col-1]:
                    stack.append(board[row][col-1])
                else:
                    stack.pop()
                    pung += 2
            else:
                stack.append(board[row][col - 1])
            board[row][col-1] = 0
    return pung

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))