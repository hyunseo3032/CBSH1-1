# Codeup 1416 이진수변환
n = int(input())
d = []
if n == 0:
    d.append(0)
while n > 0:
    d.append(n%2)
    n //= 2
for i in range(len(d)-1, -1, -1):
    print(d[i], end = '')