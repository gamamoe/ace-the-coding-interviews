# N = 총 마리수, nums = 폰켓몬 종류번호 담긴 배열
# 목적: N/2마리의 폰켓몬 선택 방법 중, 가장 많은 종류의 폰켓몬 선택한 경우의 개수 return
# idea: set으로 변환한 다음 N개수와 비교해서 값 출력
def solution(nums):
    yardstick = len(nums) // 2
    return yardstick if yardstick <= len(set(nums)) else len(set(nums))