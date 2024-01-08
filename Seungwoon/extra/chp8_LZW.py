# ord('A') = 65  -> ord()값에 -64 를 반영
# 새 글자는 27부터 반영되어 1씩 증가하며 추가

def solution(msg):
    dt = {chr(i): i - 64 for i in range(65, 91)}  # {전체 알파벳 : 1~26 숫자} 선입력
    answer = []
    w = msg[0]  # w = 현재 글자
    for c in msg[1:]:  # c = 다음 글자
        wc = w + c  # (w+c) 라는 글자 정의
        if wc in dt:  # 만약 (w+c)가 이미 있는거라면
            w = wc  # (w+c) + c 구조로 확장
        else:  # (w+c)라는 글자가 없다면
            answer.append(dt[w])  # 현재 문자열 값 업데이트 (유일 업데이트 코드)
            dt[wc] = len(dt) + 1  # (w+c) 값 업데이트
            w = c  # w 재정의
    answer.append(dt[w])  # 마지막 남은 값 업데이트

    return answer