num_of_pokemons, num_of_problems = [int(x) for x in input().split(" ")]

id_by_name = {}
name_by_id = {}
for i in range(num_of_pokemons):
    pokemon_name = input()
    id_by_name[pokemon_name] = i + 1
    name_by_id[i + 1] = pokemon_name

answer = []
for _ in range(num_of_problems):
    problem = input()

    if problem.isdigit():
        answer.append(name_by_id[int(problem)])
    else:
        answer.append(str(id_by_name[problem]))

print("\n".join(answer))
