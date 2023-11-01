import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    dp[start] = 1
    for i in graph[start]:
        if dp[i] == -1:
            dp[start] += dfs(i)
    return dp[start]


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cnt = 0
dp = [-1] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(R)
for _ in range(Q):
    print(dp[int(input())])