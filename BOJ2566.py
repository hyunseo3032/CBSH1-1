# 백준 2566 - 최댓값

d = [[0]*9 for _ in range(9)]

r=c=0
for i in range(9):
    t = list(map(int, input().split()))
    for j in range(9):
        d[i][j] = t[j]
        if d[r][c] < d[i][j]:
            r = i
            c = j
print(d[r][c])
print(r+1, c+1)