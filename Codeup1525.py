# Codeup 1525 – 크레이지 아케이드

d1 = []
for j in range(10):
    dd = list(map(int, input().split()))
    d1.append(dd)
d2 = [[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        d2[i][j] = d1[i][j]
for i in range(10):
    for j in range(10):
        a = True
        b = True
        c = True
        d = True
        if d1[i][j] > 0:
            for k in range(d1[i][j]+1):
                if j+k >= 10 or d1[i][j+k] == -1:
                    a = False
                if j-k < 0 or d1[i][j-k] == -1:
                    b = False
                if i+k >= 10 or d1[i+k][j] == -1:
                    c = False
                if i-k < 0 or d1[i-k][j] == -1:
                    d = False
                if a:
                    d2[i][j+k] = -2
                if b:
                    d2[i][j-k] = -2
                if c:
                    d2[i+k][j] = -2
                if d:
                    d2[i-k][j] = -2
dead = [0]*9

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x-=1
    y-=1
    if d2[x][y] == -2:
        dead[i] = 1
    else:
        d2[x][y] = i+1

for i in range(10):
    for j in range(10):
        print(d2[i][j], end = ' ')
    print()
print("Character Information")
for i in range(n):
    print("player", i+1, end = ' ')
    if dead[i] == 1:
        print("dead")
    else:
        print("survive")