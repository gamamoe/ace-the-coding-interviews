# "U X": 위로 X칸, "D X": 밑으로 X칸, "C": 삭제 후 바로 아래 행 선택(없으면 바로 윗행 선택)
# "Z": 최근 삭제 행 복구. 선택 행 그대로   -> 삭제된 행을 기록하는 deque 필요
# 정수 n: 원본 표 행의 개수.
# 정수 k: 기본 선택된 행 위치 -> 코드에서는 인덱스 위치
# cmd: 명령어들 (문자배열)   -> 명령어를 deque로 해보자
# 목표: 모든 명령어 후, 원본과 이후의 결과를 비교해서 각 행의 삭제여부 문자열로 붙여서 출력
# 행 0이 되는 경우 없음!
# 효율성 point!!: 실제 배열 바꾸는건 마지막에 저장된 인덱스로만 수행하기
from collections import deque


def solution(n, k, cmd):
    answer = ['O'] * n  # 답안 문자열(원본) 리스트로 세팅
    cmd = deque(cmd)  # cmd deque화
    logs = []  # 삭제처리된 history 기록 (stack연산)

    while cmd:  # 비어있지 않으면 계속 진행
        if 'D' in cmd[0]:
            action = cmd.popleft()
            k += int(action[1:])
            k = min(k, n - 1)
        elif 'U' in cmd[0]:
            action = cmd.popleft()
            k -= int(action[1:])
            k = max(k, 0)
        elif cmd[0] == 'C':  # 삭제하고 바로 아래 행 선택!
            cmd.popleft()
            logs.append(k)  # 삭제된 것 인덱스 기록
            if 'O' not in answer[k:]:
                k = max(i for i, val in enumerate(answer[:k]) if val == 'O')
            else:
                k = k + answer[k:].index('O')
        elif logs and cmd[0] == 'Z':
            cmd.popleft()
            logs.pop()  # popleft()아님

        else:
            continue

    for i in logs:  # 최종 남은 것만 갱신
        answer[i] = 'X'

    return ''.join(answer)