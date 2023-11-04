n = int(input())

dp = [2]
for i in range(1, 16):
    dp.append(dp[-1] * 2 - 1)
print(dp[n] ** 2)