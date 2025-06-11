import sys
input = sys.stdin.readline

k, n = map(int, input().split())
t = list(map(int, input().split()))

memo = [0]*n
fib  = [0]*n
for i in range(k):
    if i == 0: memo[i] = t[i]
    else: memo[i] = memo[i-1]+t[i]
    fib[i] = t[i]

for i in range(k, n):
    fib[i] = (memo[i-1]-memo[i-k-1])%100007
    memo[i] = (memo[i-1]+fib[i])%100007
print(fib[n-1])
