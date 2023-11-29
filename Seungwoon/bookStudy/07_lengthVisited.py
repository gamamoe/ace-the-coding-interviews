# 목적 : 움직인 거리 중복 제외하고 측정
# dirs: 움직이는 방향. 밖을 벗어나면 무시됨
# [0,0]은 [5,5]로 바꾸어 음수 좌표를 대체 可
# 그러나 음수좌표를 그대로 활용하는 방법도 可
# 주의점: 점(좌표)가 아니라 지나온 길(선분)을 체크해야함

def solution(dirs):
    move = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}  # 상하좌우 dict, tuple로 저장
    visited = set()  # 중복을 제거하는 set 설정
    x, y = 0, 0
    for step in dirs:
        nx, ny = x + move[step][0], y + move[step][1] #nx, ny 값 갱신
        go = (x, y, nx, ny)  # 내가 가는 것
        back = (nx, ny, x, y) # 반대로 오는 경우도 같은 의미(지나온 거리 체크 위함)
        if -5 <= nx <= 5 and -5 <= ny <= 5: # nx,ny가 범위 안에 있으면
            x, y = nx, ny # x,y 값 갱신
     #       if go not in visited and back not in visited:
     # 이걸 위에 조건문에 같이 걸면 중복 이동을 안하게되므로 오작동을 일으킴.
     # 여기서 중복 이동은 可, 중복이동한 거리를 포함시키지 않을 뿐.
     # 이 조건을 if로 따로 두고 visted.add를 넣을 수도 있지만 없어도 큰 상관은 없음
            visited.add(go)
            visited.add(back)  # 지나온 거리를 set에 기록
    return len(visited) // 2
    # 1 step당 거리가 2개씩 기록되었으므로 전체 길이에서 2를 나누면 거리값이 나옴
    # d를 따로 설정할 필요가 없다!