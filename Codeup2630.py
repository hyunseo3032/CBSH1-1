# Codeup 2630 – 삼각화단 만들기(Adv)

n = int(input())

s, e, cnt, mx, mn = 0, 0, 0, 0, 0
if n % 3 == 0:
    s = n//3
else:
    s = n//3+1
    
if n % 2 == 0:
    e = n//2-1
else:
    e = n//2

for i in range(s, e+1):
    mx = i
    if (n-i)%2 == 0:
        mn = (n-i)//2
    else:
        mn = (n-i)//2+1
    cnt += (mx-mn+1)
print(cnt)