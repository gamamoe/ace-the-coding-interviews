# enroll = 각 판매원 이름 // referral = 각 판매원의 추천인 // seller = 판매자 // amount = 판매량
# 칫솔 1개당 100원 -> amount * 100 = 얻은 수익
# 추천인 없으면 '-'
# 목적: 각 판매원이 받은 이득 리스트 출력
# dt1 = {회원 : 추천인} // dt2 = {회원 : 금액}
# dt2가 정답틀
def solution(enroll, referral, seller, amount):
    dt1 = dict(zip(enroll, referral)) # {회원 : 추천인}
    dt2 = dict(zip(enroll, [0]*len(enroll))) # {회원 : 초기값 0원}

    for i in range(len(seller)):
        money = amount[i] * 100
        current_name = seller[i]
        while money >= 1 and current_name != '-': #돈이 1원 이상이고 '-'가 아닐 때 계속 진행
            dt2[current_name] += money - money // 10
            current_name = dt1[current_name]
            money //= 10

    return [dt2[name] for name in enroll]