# Codeup 1512 – 숫자등고선

n = int(input())
x, y = map(int, input().split())
x, y = x-1, y-1

for i in range(n):
    for j in range(n):
        print(abs(i-x)+abs(j-y)+1, end = ' ')
    print()