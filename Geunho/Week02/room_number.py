import sys

N = sys.stdin.readline().strip()
number_counter = {
    "0": 1,
    "1": 1,
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
    "6": 2,
    "7": 1,
    "8": 1,
}
answer = 1


for char in N:
    if char == "9":
        char = "6"

    if number_counter[char] == 0:
        answer += 1
        for key in number_counter.keys():
            if key == "6":
                number_counter[key] += 2
            else:
                number_counter[key] += 1

    number_counter[char] -= 1

print(answer)
