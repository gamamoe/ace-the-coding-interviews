def hash_func(string, m):
    s = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
                'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q': 17, 'r':18, 's':19,
                't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    hash_value = 0
    for i, alphabet in enumerate(string):
        hash_value += (s[alphabet] * (31 ** i)) % m
    hash_value %= m
    return hash_value
def solution(string_list, query_list):
    answer = []
    m = 1000000007
    hashtable = [0] * m
    for string in string_list:
        hashtable[hash_func(string, m)] = 1

    for query in query_list:
        if hashtable[hash_func(query, m)]:
            answer.append(True)
        else:
            answer.append(False)
    return answer

print(solution(["apple", "banana", "cherry"],
               ["banana", "kiwi", "melon", "apple"]))
