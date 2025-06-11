# Codeup 3702 – 파스칼의 삼각형 2

r, c = map(int, input().split())
memo = [[1]*51 for i in range(51)]

for i in range(1, r):
    for j in range(1, c):
        memo[i][j] = (memo[i-1][j] + memo[i][j-1])%100000000
print(memo[r-1][c-1])