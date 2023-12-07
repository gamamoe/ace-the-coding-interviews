# 목표: 작동시킨 후 터져 사라진 인형의 개수 찾기
# board: 2차원 배열. 움직이는 공간. 숫자는 각 인형 type.(1~100). 0은 빈칸
# moves: 크레인 작동한 곳
# 인형이 없는데 작동한 경우 아무일도 일어나지 않는다.
# 한번 moves로 작동하면 100% 실행된다.

def solution(board, moves):
    # zip: 각 행 tuple로 전환. 여기서 *로 transpose. filter로 stack 정리
    lst = [list(filter(lambda x: x != 0, reversed(col))) for col in zip(*board)]
    st = [0]      # 바구니 설정 (비어있으면 인덱스 오류 생기므로 넣음)
    answer = 0
    for i in moves:
        if lst[i-1]: # moves의 값은 python index처럼 0부터 시작하지 않으므로 i-1
            k = lst[i-1].pop() # pop된 값 저장
            if k != st[-1]: # st의 최근값과 같은지 여부 검사
                st.append(k) # 안같으면 추가
            else:  # 같으면
                st.pop() # 최근값 pop
                answer += 2 # answer값 +2
        else: # 리스트가 비어있는경우 무시
            continue

    return answer