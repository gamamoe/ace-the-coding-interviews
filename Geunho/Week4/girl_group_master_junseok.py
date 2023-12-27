import sys
from collections import defaultdict

N, M = [int(x) for x in sys.stdin.readline().split()]
team_name_by_member_name = {}
member_names_by_team_name = defaultdict(list)
for _ in range(N):
    team_name = sys.stdin.readline().strip()
    num_of_members = int(sys.stdin.readline().strip())

    for _ in range(num_of_members):
        member_name = sys.stdin.readline().strip()

        team_name_by_member_name[member_name] = team_name
        member_names_by_team_name[team_name].append(member_name)

answer = []
for _ in range(M):
    problem = sys.stdin.readline().strip()
    problem_type = int(sys.stdin.readline().strip())

    if problem_type == 1:
        answer.append(team_name_by_member_name[problem])
    else:
        answer.extend(sorted(member_names_by_team_name[problem]))

print("\n".join(answer))
