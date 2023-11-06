INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
paths = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b], graph[b][a] = cost, cost
    paths[a][b], paths[b][a] = b, a
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            temp = graph[a][k] + graph[k][b]
            if graph[a][b] > temp:
                graph[a][b] = temp
                paths[a][b] = paths[a][k]
for i in range(1, n + 1):
    paths[i][i] = "-"
for i in paths[1:]:
    print(*i[1:])