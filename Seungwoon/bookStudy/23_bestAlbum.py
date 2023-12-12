# 장르 > 최다재생 > 낮은 고유번호(=파이썬 인덱스)
# 목표: 이 기준으로 들어갈 노래의 고유번호 순서
# 다른 두 장르가 동일 재생횟수인 경우 X (같은 장르내에서는 동일 횟수 可)
# 구조: {인덱스 : genres} -> plays 맵핑.  plays를 list로 받아야 함
from collections import defaultdict


def solution(genres, plays):
    answer = []  # 정답 통
    dt1 = defaultdict(list)  # {장르 : [재생 횟수]}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        dt1[genre].append((play, i))  # (재생 횟수, 고유번호)를 리스트에 저장

    # value값이 큰 순서대로 key값 내림차순 정렬
    dt1 = dict(sorted(dt1.items(), key=lambda x: sum(p for p, _ in x[1]), reverse=True))

    # 각 value값을 큰 순서대로 내림차순 정렬
    dt1 = {genre: sorted(values, key=lambda x: -x[0])[:2] for genre, values in dt1.items()}

    # 정답에 추가 (고유번호 뽑기)
    for values in dt1.values():
        answer.extend([index for _, index in values])

    return answer