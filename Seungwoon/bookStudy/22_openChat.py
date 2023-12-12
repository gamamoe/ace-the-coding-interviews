# 닉네임 변경 법: 나갔다가 새 닉네임으로 들어오기 or 채팅방 내 닉네임 변경
# 닉네임 변경 효과: 기존 출력된 메세지의 닉네임도 전부 변경
# 중복 닉네임을 허용한다. '유저id'로 구분한다.

# record: 채팅방 출입기록, 닉 변경 기록. 나간 유저가 닉변경하는 경우는 없음
# record 구조: "Enter or Leave or Change  // uid####  // 닉네임"
# 목적: record 전부 처리한 후 나올 최종 출력물?

# dict를 갱신하는 uid : nick 구조로 dict 만듦 - > 최종 id와 nick 정리한 dict
from collections import defaultdict

def solution(record):
    dt = defaultdict(str) # id : 최종 nick 정리 통
    answer = [] # 정답 메세지 통
    for i in record:
        cmd, uid, *nick = i.split() # 항상 3개가 아님. leave는 nick이 없으므로 *를 붙임
# id를 key로 받고 nick(value)를 갱신 -> change, 나갔다들어오기 순서 자동 포함
        if nick:  # 제일 중요한 부분! nick이 없는 경우의 갱신이 이상해지거나 런타임 에러!!
           dt[uid] = nick # *nick는 나머지처리이므로 list로 value값이 저장됨

    for i in record:
        cmd, uid, *nick = i.split()
        if cmd == 'Enter':  # dt의 value가 list로 저장되었으므로 [0]을 붙인다.
            answer.append(f"{dt[uid][0]}님이 들어왔습니다.")
        elif cmd == 'Leave':
            answer.append(f"{dt[uid][0]}님이 나갔습니다.")
    return answer