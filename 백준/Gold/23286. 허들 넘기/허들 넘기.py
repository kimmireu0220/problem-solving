INF = int(1e9)
n, m, t = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], max(graph[a][k], graph[k][b]))
for _ in range(t):
    a, b = map(int, input().split())
    print(graph[a][b]) if graph[a][b] != INF else print(-1)
