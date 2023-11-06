def solve(start, end):
    return graph[start][end]
    

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for _ in range(M):
    u, v, b = map(int, input().split())
    graph[u][v] = 0
    graph[v][u] = 0 if b else 1
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(solve(s, e))