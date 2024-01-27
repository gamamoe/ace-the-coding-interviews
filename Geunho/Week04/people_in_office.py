num_of_logs = int(input())

people_in_office = set()
for _ in range(num_of_logs):
    name, command = input().split(" ")
    if command == "enter":
        people_in_office.add(name)
    else:
        people_in_office.remove(name)

print("\n".join(sorted(people_in_office, reverse=True)))
