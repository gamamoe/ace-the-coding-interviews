def solution(answers):
    result = []
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    scores = [0, 0, 0]
    for i, pattern in enumerate(patterns):
        length = len(pattern)
        for j, answer in enumerate(answers):
            if answer == pattern[j%length]:
                scores[i] += 1
    # 최고 득점자 반환
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            result.append(i+1)
    return result

# def solution(answers):
#     answer = []
#     scores = [0, 0, 0]
#     length = len(answers)
#     # 1번 수포자
#     sheet1 = [1,2,3,4,5] * (length//5 + 1)
#     sheet1 = sheet1[:length]
#     for i in range(len(sheet1)):
#         if sheet1[i] == answers[i]:
#             scores[0] += 1
#     # 2번 수포자
#     sheet2 = [2,1,2,3,2,4,2,5] * (length//8 + 1)
#     sheet2 = sheet2[:length]
#     for i in range(len(sheet2)):
#         if sheet2[i] == answers[i]:
#             scores[1] += 1
#     # 3번 수포자
#     sheet3 = [3,3,1,1,2,2,4,4,5,5] * (length//10 + 1)
#     sheet3 = sheet3[:length]
#     for i in range(len(sheet3)):
#         if sheet3[i] == answers[i]:
#             scores[2] += 1
#     # 최고 득점자 반환
#     for i in range(3):
#         if scores[i] == max(scores):
#             answer.append(i+1)
#     return answer

answers1 =[1,2,3,4,5]
answers2 = [1,3,2,4,2]

print(solution(answers1))
print(solution(answers2))