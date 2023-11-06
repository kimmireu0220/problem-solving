import sys
INF = int(1e8)
def input(): return sys.stdin.readline().rstrip()

n,m = map(int, input().split())
graph =[[INF] * (n+1) for _ in range(n+1)]
node = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c, = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    node[a][b] = b
    node[b][a] = a

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                node[a][b] = node[a][k]

for i in range(1,n+1):
    node[i][i] = '-'

for array in node[1:]:
    print(*array[1:])