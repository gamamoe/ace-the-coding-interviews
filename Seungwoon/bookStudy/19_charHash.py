# ➊ polynomial hash를 구현한 부분
def polynomial_hash(str): # 해시값 만드는 함수
    p = 31  # 메르센 소수
    m = 1_000_000_007  # 버킷 크기; 문제에 주어진 제약조건
    hash_value = 1 # 값 할당
    for char in str: #  str의 글자 하나하나를 점검한다.
        # 책 기존 식에 직관적으로 유사하게 구현. 이렇게해도 작동은 된다.(해시함수 목적에 부합한다면)
        hash_value = (hash_value * p * ord(char)) % m # ord(): 문자값의 유니코드 반환
# honer's rule에 따라 hash_value = (hash_value * p + ord(char)) % m 라는 원본 코드가 틀린 것이 아님.
    return hash_value

def solution(string_list, query_list):
    # ➋ string_list의 각 문자열에 대해 다항 해시값을 계산
    hash_list = [polynomial_hash(str) for str in string_list]

    # ➌ query_list의 각 문자열이 string_list에 있는지 확인
    result = [] # 정답지 통
    for query in query_list:
        query_hash = polynomial_hash(query)
         # 대응되면 True, 아니면 False
        result.append(query_hash in hash_list)

    return result


assert solution(['apple','banana','cherry'], ['banana','kiwi','melon','apple']) == [True,False,False,True], '출력값1 에러'