# Codeup 1510 – 홀수 마방진

n = int(input())
d = [[1]*n for i in range(n)]
c = 2
i, j = 0, n//2

while c <= n*n:
    if (c-1) % n != 0:
        i -= 1
        j += 1
    else:
        i += 1
    if i < 0: i = n-1
    if j >= n: j = 0
    d[i][j] = c
    c+=1
for k in d:
    print(*k)