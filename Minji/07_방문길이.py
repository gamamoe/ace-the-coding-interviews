# 캐릭터가 처음 걸어본 길의 길이를 구하는 문제
# -> 반복된 부분은 무시

def solution(dirs):
    answer = set() # 중복되는 좌표 제거
    x = y = 5 # 음수의 포지션을 양수로 변경하기 위해 중심을 5로 설정
    # 지나온 길이기 때문에 지난 좌표와 지나온 좌표가 모두 필요
    nx = ny = 0 # 명령어의 의해 값이 변경되기 때문에 0으로 초기화
    list_dirs = list(dirs)
    
    for i in range(len(list_dirs)):     
      # 좌표평면의 경계(0-10)을 넘어가는 명령어 무시     
      if 0 < y < 10:
        # 받은 명령어로 좌표 이동
        if list_dirs[i] == "U":
          nx, ny = x, y + 1  
        elif list_dirs[i] == "D":
          nx, ny = x, y - 1
          
      if 0 < x < 10:
        if list_dirs[i] == "R":
          nx, ny = x + 1, y 
        elif list_dirs[i] == "L":
          nx, ny = x - 1, y
      
      # 방향성이 없음, A -> B, B -> A도 추가
      answer.add((x, y, nx, ny)) # set()에 add()
      answer.add((nx, ny, x, y))
      x = nx # 좌표 이동으로 update
      y = ny

    # 방향성 때문에 데이터를 두번 넣었기 때문에
    return len(answer) // 2


dirs = "ULURRDLLU"
solution(dirs)

dirs2 = "LULLLLLLU"
solution(dirs2)
