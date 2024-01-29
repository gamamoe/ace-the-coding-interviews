# https://www.acmicpc.net/problem/9372
# 1) 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다
# 2) 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다
# 따라서 최소 신장 트리를 의미하며, Edge의 수 (즉, 비행기 수)는 항상 국가 갯수 - 1이 된다
import sys

num_of_test_cases = int(sys.stdin.readline())
answer = []
for _ in range(num_of_test_cases):
    num_of_countries, num_of_planes = [int(x) for x in sys.stdin.readline().split()]

    for _ in range(num_of_planes):
        country1, country2 = [int(x) for x in sys.stdin.readline().split()]
    answer.append(str(num_of_countries - 1))

print("\n".join(answer))
