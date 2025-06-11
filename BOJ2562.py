# 백준 2562 – 최댓값

d = [int(input()) for _ in range(9)]
idx = 0
for i in range(9):
    if d[idx] < d[i]:
        idx = i
print(d[idx], idx+1, sep='\n')
