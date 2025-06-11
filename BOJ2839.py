# 백준 2839 - 설탕 배달

n = int(input())
dp = [-1]*5050
dp[3]=dp[5]=1
for i in range(6, n+1):
    if dp[i-3] == -1 and dp[i-5] == -1:
        dp[i] = -1
    elif dp[i-3] == -1:
        dp[i] = dp[i-5]+1
    elif dp[i-5] == -1:
        dp[i] = dp[i-3]+1
    else:
        dp[i] = min(dp[i-5], dp[i-3])+1
print(dp[n])