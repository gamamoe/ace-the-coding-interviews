# 신고 횟수 제한 X: 단, 한 번당 한 명 유저 신고.
# 중복 신고 可: 단, 중복 신고는 1회처리
# k번 이상 신고된 유저 -> 정지 & 이 유저를 신고한 모든 유저에게 이 사실 알림
# id_list: 전체 유저 // report: 누가 누굴 신고했는지 // k = 정지 기준
# 목표: id_list 각 유저들이 메일을 받은 횟수 출력

# 출력을 위한 필요정보: 각 유저가 신고한 ID, 각 유저별 신고당한 횟수
# dt1 = {유저id : 신고한 id} -> 여기서 dt2 = {유저id : 신고당한 횟수} 도출(dt1로 중복신고 처리)
# dt2에서 정지된id 리스트 lst 도출 -> dt1 value가 lst에 있는 횟수 출력(목표)

from collections import defaultdict

def TrialSolution(id_list, report, k): # 책 안보고 혼자서 쓴 코드
    # dt1 = {유저id : [신고한 id 리스트]}  + 정렬기준은 id_list
    dt1 = defaultdict(list)
    for key in id_list:  # id_list정렬 기준으로 key값 통 생성
        dt1[key] = []
    for i in report:  # value값 반영
        dt1[i.split()[0]].append(i.split()[1])

    # dt1을 set으로 value값 중복 제거
    for key, val in dt1.items():
        dt1[key] = list(set(val))

    # dt2 = {유저id : 신고당한 횟수} 도출
    dt2 = defaultdict(int)
    for val in dt1.values():
        for i in range(len(val)):
            dt2[val[i]] += 1

    # dt2에서 정지된id 리스트 lst 도출
    lst = [key for key in dt2 if dt2[key] >= k]

    # dt1 value와 lst를 비교하여 answer 갱신
    answer = [0] * len(id_list)  # 기본값은 0
    for i, key in enumerate(id_list):
        for reported_id in dt1[key]:  # dt1[key] = 신고id 리스트
            if reported_id in lst:  # lst에 있으면 값 +1
                answer[i] += 1

    return answer



def solution(id_list, report, k): # 저자의 풀이를 defaultdict으로 바꾸어 표현한 코드
    dt = defaultdict(set)     # dt = {신고당한유저 : 신고유저 집합}
    mail_count = defaultdict(int)  # mail_count = {신고한 유저: 메일받은 횟수}

    for i in report: # {신고당한유저 : 신고유저 집합}
        val, key = i.split()  # val(신고한 유저)과 key(신고당한유저)의 순서에 주목한다.
        dt[key].add(val)
    # for key, val in dt.items():  dt 생김새를 보려면 이 코드가 필요하다.(없으면 JSON오류)
    #     dt[key] = list(set(val))

    for who_reported in dt.values(): # 신고한 유저들 집합에 대해서
        if len(who_reported) >= k: # 이용정지 조건에 해당되는 유저가 key라면,
            for uid in who_reported: # 그 유저들 신고한 사람들에게
                mail_count[uid] += 1  # 메일이 전송된다.
    answer = []
    for i in range(len(id_list)):  # id_list로 순회해서 자동 정렬
        if id_list[i] not in mail_count: # 메일받은 유저가 아니면
            answer.append(0) # 0으로 입력
        else:
            answer.append(mail_count[id_list[i]])

    return answer



def ShortSolution(id_list, report, k): # 숏코딩이 돋보이는 타인의 코드.
    answer = [0] * len(id_list)     # 정답통 (default = 0)
    reports = {x : 0 for x in id_list} # {기존 id : 신고당한 횟수}

    for i in set(report): # 중복방지 set
        reports[i.split()[1]] += 1

    for i in set(report):
        if reports[i.split()[1]] >= k: # key가 정지된 이용자이면
            answer[id_list.index(i.split()[0])] += 1
            # 신고한 유저가 있는 id_list의 index위치에 +=1 (메일 개수)

    return answer