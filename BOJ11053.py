# O(n^2)
n = int(input())
d = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if d[i] > d[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
# O(nlogn)
n = int(input())
d = list(map(int, input().split()))
lis = []

for x in d:
    l = 0
    r = len(lis)
    while l < r:
        m = (l+r)//2
        if lis[m] < x: l = m+1
        else: r = m
    if l == len(lis): lis.append(x)
    else: lis[l] = x
print(len(lis))