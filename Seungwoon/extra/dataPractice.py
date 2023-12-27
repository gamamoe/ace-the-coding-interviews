# 문제1:  고객 정보에 존재 하는 전체 고객의 수  -> problem_1.json 로 total값은?
import os # 디렉토리 설정
import json  # json 파일 다루기
with open("data/input/customer.json", 'r') as file:  # 데이터 read 호출
    data = json.load(file)

# 문제 1번 dict 생성
problem1 = {
    "total" : len(data)
}

path1 = os.path.join("data/output", "problem_1.json")
with open(path1, 'w') as f: # p1 write as json
    json.dump(problem1, f)




# 문제2: 현재 고객 상태(status)가 휴면(dormant)인 고객 ID 리스트 오름차순 출력
lst = [dt[key] for dt in data for key in dt if dt['status'] == 'dormant' and key == 'customer_id']
lst.sort() # 오름차순 정렬

path2 = os.path.join("data/output", "problem_2.json")
with open(path2, 'w') as f: # p1 write as json
    json.dump(lst, f)