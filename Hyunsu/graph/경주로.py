import heapq

#제출시테스트 실패 케이스 테스트 24 〉	실패 (0.11ms, 10.4MB) 92%


def solution(board):
    dy=[-1,0,1,0] #북동남서
    dx=[0,1,0,-1]
    hq= []
    heapq.heappush(hq, (0,None,0,0))
    visited = [ [float("inf")]*len(board) for i in range(len(board))  ]
    while(hq):
        w, axis, y, x =heapq.heappop(hq)
        _axis = axis 
        print(w, axis, y, x)
        for i in range(4):
            nx= x+dx[i]
            ny = y+dy[i]

            if(nx<0 or ny<0 or nx>=len(board) or ny>=len(board) or board[ny][nx] ==1):
                continue 
            if axis == None: 
                if( ny == y and nx!=x):
                    _axis = "x"
                elif(nx == x and ny!=y):
                    _axis = "y"
            next_axis = _axis
            if( ny == y and nx!=x):
                next_axis = "x"
            elif(nx == x and ny!=y):
                next_axis = "y"  

            isCorner =  _axis != next_axis
            corner_w =  500 if isCorner else 0 
            next_w = w+100+corner_w
            # visited 값과 비교 하여 작으면  visited 값 갱신
            if next_w <= visited[ny][nx]:
                visited[ny][nx] = next_w
                heapq.heappush(hq, (next_w, next_axis, ny, nx)) #heapq에 넣기 
    print(visited[-1][-1])        
    return visited[-1][-1]









# solution([[0,0,0],[0,0,0],[0,0,0]])
# solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
# solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])