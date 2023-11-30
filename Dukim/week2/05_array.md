# 05 배열
## 05-1 배열 개념
* 배열 선언
  ```python
  arr = [0, 0, 0, 0, 0, 0]
  arr = [0] * 6
  arr = list(range(6)) # 리스트 생성자 이용
  arr = [0 for _ in range(6)] # 리스트 컴프리헨션 이용 
  ```
* 배열과 차원
  - 차원과 무관하게 메모리에 연속 할당
  ```python 
  # 3x2 리스트 생성 예
  arr = [[i]*2 for i in range(3)]
  # [[0,0],[1,1],[2,2]]
  ```
## 05-2 배열의 효율성
* 배열 연산의 시간 복잡도
  - 데이터 접근 : O(1)
  - 맨 뒤 삽입 : O(1)
  - 맨 앞 삽입 : O(N)
  - 중간 삽입 : O(N)
## 05-3 자주 활용하는 리스트 기법
* 리스트에 데이터 추가
  - append() 메서드와 `+`연산자로 추가
  - insert() 메서드로 삽입
  ```python 
  list1 = [1,2,3,4]
  list1.append(5) # [1,2,3,4,5]
  list2 = [6]
  list3 = list1 + list2 # [1,2,3,4,5,6]
  list3.insert(2,0) # [1,2,0,3,4,5,6]
  ```
* 리스트에서 데이터 삭제
  - pop() 메서드로 특정 위치의 데이터 추출
  - remove() 메서드로 특정 데이터 삭제
  ```python
  list4 = [1,2,3,4,5]
  poped_item = list4.pop(2) # poped_item : 3, list4 : [1,2,4,5]
  list5 = [2,3,2,3,2]
  list5.remove(2) # [3,2,3,2]
  list5.remove(2) # [3,3,2]
  ```
* 리스트 컴프리헨션으로 데이터에 특정 연산 적용
  - 리스트 제곱 연산 예제
  ```python
  list6 = [1,2,3] 
  [n**2 for n in list6] # [1,4,6] 
  ```
* 유용한 리스트 연관 메서드
  - 리스트 정렬 : list.sort(), sorted(list)
  - 리스트의 전체 개수 : len()
  - 특정 데이터가 처음 등장한 인덱스 반환 : index()
  - 특정 데이터 개수를 반환 : count()
  ```python
  # 정렬
  fruits = ['apple', 'banana', 'cherry', 'apple', 'orange', 'banana', 'kiwi']
  fruits.sort() # mutable
  print(fruits) # ['apple', 'apple', 'banana', 'banana', 'cherry', 'kiwi', 'orange']
  fruits.sort(reverse=True) # mutable 
  print(fruits)  # ['orange', 'kiwi', 'cherry', 'banana', 'banana', 'apple', 'apple']
  new_fruits = sorted(fruits) # immutable
  print(fruits) # 변경되지 않음
  print(new_fruits) # ['apple', 'apple', 'banana', 'banana', 'cherry', 'kiwi', 'orange']
  # 개수
  print(len(fruits)) # 7
  # index
  print(fruits.index('kiwi')) # 1
  # count
  print(fruits.count('banana')) # 2
  ```
## 05-4 몸풀기 문제
* 문제01 배열 정렬하기
  - 파이썬에 구현된 sort() 메서드의 시간복잡도 : O(NLogN) 
* 문제02 배열 제어하기
  - set() 함수의 시간복잡도 : O(N)
## 05-5 합격자가 되는 모의 테스트
* 문제03 두 개 뽑아서 더하기
  - 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/68644
* 문제04 모의고사
  - 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42840
  ```python
  def solution(answers):
    pattern_1 = [1,2,3,4,5,]
    pattern_2 = [2,1,2,3,2,4,2,5,]
    pattern_3 = [3,3,1,1,2,2,4,4,5,5,]

    same_count = [0, 0, 0]
    for idx, n in enumerate(answers):
      if pattern_1[idx % len(pattern_1)] == n:
        same_count[0] += 1
      if pattern_2[idx % len(pattern_2)] == n:
        same_count[1] += 1
      if pattern_3[idx % len(pattern_3)] == n:
        same_count[2] += 1

    max_ = max(same_count)
    return [idx+1 for idx, s in enumerate(same_count) if s==max_]
  ```
* 문제05 행렬의 곱셈
  - 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12949
* 문제06 실패율
  - 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42889
  ```python
  from collections import Counter
  
  def solution(N, stages):
    """
    :param N: stage 개수, 1~500
    :param stages: 도전자들이 도전하고 있는 stage 번호, 1~200_000
    """
    # 1 ~ N+1 challenger count
    challenger = Counter() # 스테이지별 도전자 수
    for stage in stages:  # O(n)
      challenger[stage] += 1
    print(challenger)

    failure_rate = [0]*N
    total = len(stages)
    for stage in range(1, N+1):  # 1<=N<=500
      if challenger[stage] == 0:
        failure_rate[stage-1] = 0
      else:
        failure_rate[stage-1] = challenger[stage]/total
        total -= challenger[stage]

    result = sorted(range(1, N+1), key=lambda x: failure_rate[x-1], reverse=True)
    return result 
  ```
* 문제07 방문 길이
  - 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/49994
