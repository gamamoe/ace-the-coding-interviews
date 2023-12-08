def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        if stack == []:
            stack.append(i)
        else:
            while stack and prices[stack[-1]] > prices[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            else:
                stack.append(i)
    while stack:
        answer[stack[-1]] = len(prices) - stack[-1] - 1
        stack.pop()
    return answer

print(solution([1,2,3,2,3]))
print(solution([1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 1, 2, 3]))
print(solution([12, 5, 4, 3, 2, 1, 6, 5, 2, 1, 2, 1, 0]))
# print(solution([1, 2, 3, 4, 1]))
