n = int(input())
memo = [0]*(n + 1)

def f(i):
    if i > n:
        return
    if i <= 2:
        memo[i] = 1
    else:
        memo[i] = memo[i-1] + memo[i-2]
    f(i+1)

f(1)
print(memo[n]%10009)
