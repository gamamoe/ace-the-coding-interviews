def solution(arr):
    answer = ['-'] # 빈 리스트 방지
    for i in arr:
        if answer[-1] == i:
            continue
        else:
            answer.append(i)
    return answer[1:]