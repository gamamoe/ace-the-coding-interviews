import itertools
import sys

K, L = [int(x) for x in input().split(" ")]
order_by_student_id = {}
student_id_by_order = {}
for i in range(L):
    student_id = sys.stdin.readline().strip()
    order_by_student_id[student_id] = i
    student_id_by_order[i] = student_id


answer = []
for student_id in itertools.islice(sorted(order_by_student_id.values()), 0, K):
    answer.append(student_id_by_order[student_id])

print("\n".join(answer))
