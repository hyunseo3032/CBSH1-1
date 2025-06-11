# Codeup 1440 비교

n = int(input())
d = list(map(int, input().split()))

for i in range(n):
    print(i+1, ': ', sep = '', end = '')
    for j in range(n):
        if i != j:
            if d[i] > d[j]: print("> ", end = '')
            elif d[i] < d[j]: print("< ", end = '')
            else: print("= ", end = '')
    print()