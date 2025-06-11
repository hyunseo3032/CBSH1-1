# Codeup 2632 – 계단오르기 1

n = int(input())
memo = [1, 2]

for i in range(2, n):
    memo.append(memo[i-1]+memo[i-2])
print(memo[n-1])