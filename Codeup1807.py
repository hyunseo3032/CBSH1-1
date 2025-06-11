# Codeup 1807 – 우박수 길이 (3n+1) (small)

a, b = map(int, input().split())
n = -1
l = -1

for i in range(a, b+1):
    p = i
    p_len = 1
    while p > 1:
        if p % 2 == 0:
            p //= 2
        else:
            p = 3*p+1
        p_len += 1
    if p_len > l:
        l = p_len
        n = i
print(n, l)