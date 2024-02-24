import sys

n, k = [int(x) for x in sys.stdin.readline().split()]
coins = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

answer = 0
for index in range(n - 1, -1, -1):
    num_of_coins, remainder = divmod(k, coins[index])
    answer += num_of_coins
    k = remainder

print(answer)
