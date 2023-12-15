def solution(record):
    # 1. 입력을 읽어들여서 명령처리
    # 2. 닉네임 딕셔너리? 키 = 유저아이디, 밸류 = 닉네임
    # 3. Enter user nick
    # 3.1. 닉네임 딕셔너리 추가/변경
    # 3.2. 리스트에 ["Enter", "userid"] 추가
    # 4. Leave user
    # 4.1. 리스트에 ["Leave", "userid"] 추가
    # 5. change user nick
    # 5.1. 닉네임 딕셔너리 변경
    # 6. 다 끝나고 나서, 리스트 읽으면서, 메시지 리스트 생성

    nick_dic = {}
    messages = []
    for info in record:
        rec = info.split(' ')
        if rec[0] == "Enter":
            nick_dic[rec[1]] = rec[2]
            messages.append([1, rec[1]])
        elif rec[0] == "Leave":
            messages.append([0, rec[1]])
        elif rec[0] == "Change":
            nick_dic[rec[1]] = rec[2]
    answer = []
    for message in messages:
        if message[0] == 1:
            answer.append(f"{nick_dic[message[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nick_dic[message[1]]}님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prode", "Leave uid1234",
                "Enter uid1234 Prodo", "Change uid4567 Ryan"]))