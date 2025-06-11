# Codeup 2605 – 캔디팡

d = []
visit = [[False]*7 for _ in range(7)]
cnt = 0

for _ in range(7):
    dd = list(map(int, input().split()))
    d.append(dd)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(7):
    for j in range(7):
        if visit[i][j]:
            continue
        s = [[i, j]]
        visit[i][j] = True
        size = 1
        val = d[i][j]

        while len(s) > 0:
            x, y = s.pop()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0 <= nx < 7 and 0 <= ny < 7:
                    if not visit[nx][ny] and d[nx][ny] == val:
                        visit[nx][ny] = True
                        s.append([nx, ny])
                        size += 1
        if size >= 3:
            cnt += 1
print(cnt)