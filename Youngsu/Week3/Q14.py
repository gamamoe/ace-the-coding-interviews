def solution(n, k, cmd):
    answer = ''
    stack = []
    index = k
    table = [ i for i in range(n)]
    for i, c in enumerate(cmd):
        if c[0] == 'U':
            index -= int(c[2])
        elif c[0] == 'D':
            index += int(c[2])
        elif c == 'C':
            stack.append([index, table.pop(index)])
            if index == len(table):
                index -= 1
        elif c == 'Z':
            i_insert, value = stack.pop()
            table.insert(i_insert, value)
            if index > i_insert:
                index += 1
    offset = 0
    for i in range(n):
        if i == table[i - offset]:
            answer += "O"
        else:
            answer += "X"
            offset += 1
    return(answer)

# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))