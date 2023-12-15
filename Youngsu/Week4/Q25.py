from itertools import combinations

def solution(orders, course):
    answer = []
    course_menu = {}
    for order in orders:
        for num in course:
            if num not in course_menu:
                course_menu[num] = {}
            for combi in combinations(sorted(order), num):
                if combi not in course_menu[num]:
                    course_menu[num][combi] = 1
                else:
                    course_menu[num][combi] += 1

    for k, v in course_menu.items():
        # sorted_menu = sorted(course_menu[k].items(), key=lambda x: (x[1], x[0]), reverse=(True, False))
        sorted_menu = sorted(course_menu[k].items(), key=lambda x: x[1], reverse=True)

        if sorted_menu:
            criterion = sorted_menu[0][1]

        for i in range(len(sorted_menu)):
            if sorted_menu[i][1] == criterion and criterion > 1:
                answer.append("".join(sorted_menu[i][0]))
        answer = sorted(answer)
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
               [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
               [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"],
               [2, 3, 4]))