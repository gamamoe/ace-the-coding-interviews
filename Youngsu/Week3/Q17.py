def solution(cards1, cards2, goal):
    answer = 'Yes'
    for word in goal:
        if cards1 != [] and cards1[0] == word:
            cards1.pop(0)
        elif cards2 != [] and cards2[0] == word:
            cards2.pop(0)
        else:
            answer = "No"
    return answer

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))