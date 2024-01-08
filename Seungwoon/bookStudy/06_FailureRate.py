# 목적: 스테이지별 실패율을 내림차순으로 나열한 것을 스테이지 번호로 출력하기
# stages 원소 = 게임 내 사용자가 멈춰있는 스테이지 번호
# 결국 각 스테이지당 몇 명인지 세는 과정 = count가 필요
# 실패율의 분자 = count의 원소  / 실패율의 분모 = 전체 스테이지 개수 - 현재 count 기준 이전 count 분자 합
def solution(N, stages):
    count = []  # 각 stage당 몇명이 있는지 재정의하는 리스트
    for i in range(1, N + 1):
        count.append(stages.count(i))  # stage 1부터 유저 수 저장

    fail = []  # 실패율 리스트
    total = len(stages)  # 전체 스테이지 개수. total은 실패울의 분모값
    for j in range(len(count)):
        if j == 0:  # 첫 번째 값은 total이 분모로 온전히 들어감
            fail.append(count[j] / total)
        elif j > 0:  # 두 번째 값부터 total이 0이 아닌 조건 필요
            total -= count[j - 1]  # 분모 차감 누적
            if total != 0:  # 0이 아니라면
                fail.append(count[j] / total)  # 값 추가
            else:  # 0이면
                fail.append(0)  # 0을 추가
        else:  # 위의 조건을 벗어나면 무조건 0으로 처리
            fail.append(0)
            # 스테이지 이름 : 실패율로 dict 정의
    ndict = {key + 1: value for key, value in enumerate(fail)}
    # ndict에서 key값만 뽑고, 내림차순 value값으로 list 형성 = answer
    answer = sorted(ndict, key=ndict.get, reverse=True)
    # sorted()는 list()가 없어도 형식이 맞다면 list()를 적용해서 출력한다.
    return answer


# 효율성 좋은 책의 코드 내용 분석
def solution1(N, stages):
    # ➊ 스테이지별 도전자 수를 구함
    challenger = [0] * (N + 2)
    for stage in stages:  # stages값의 원소를 challenger의 인덱스로 받아서
        challenger[stage] += 1  # 해당 인덱스의 값에 += 1하는 것. (count보다 효율적!)
    # 계수정렬 개념과 연관있다고 한다.

    # ➋ 스테이지별 실패한 사용자 수를 계산
    fails = {}  # dict형태로 정의되었음에 유의한다!
    total = len(stages)

    # ➌ 각 스테이지를 순회하며, 실패율을 계산
    for i in range(1, N + 1):  # challenger의 0번째 인덱스는 사용안하므로 1부터 N+1 설정 유의!
        if challenger[i] == 0:  # ➍ 도전한 사람이 없는 경우, 실패율은 0
            fails[i] = 0  # 실패율의 해당 인덱스 key i에 해당하는 실패율(value)는 0으로 업데이트
        else:
            fails[i] = challenger[i] / total  # ➎ 해당 인덱스 i(key)에 해당하는 실패율(value) 정의
            total -= challenger[i]  # ➏ 다음 스테이지 실패율을 구하기 위해 현재 스테이지의 인원을 뺌

    # ➐ 실패율이 높은 스테이지부터 내림차순으로 정렬
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    # fails[x]는 x라는 key에 해당한s value값을 호출한다.
    # sorted()는 list()가 없어도 형식이 맞다면 list()를 적용해서 출력한다.

    return result

