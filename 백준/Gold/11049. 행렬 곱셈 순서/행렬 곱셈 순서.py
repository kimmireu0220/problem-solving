N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for term in range(1, N):
    for start in range(N):
        if start + term == N:
            break

        dp[start][start + term] = float("inf")
        for t in range(start, start + term):
            dp[start][start + term] = min(
                dp[start][start + term],
                dp[start][t]
                + dp[t + 1][start + term]
                + board[start][0] * board[t][1] * board[start + term][1],
            )

print(dp[0][N - 1])
