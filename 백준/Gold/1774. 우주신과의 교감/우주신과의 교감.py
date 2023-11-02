import math

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[b] = a

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
result = 0
parent = [i for i in range(n + 1)]
rockets = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        ax, ay = rockets[i]
        bx, by = rockets[j]
        cost = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
        edges.append([cost, i, j])

for _ in range(m):
    a, b = sorted(map(int, input().split()))
    edges.append([0, a, b])

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(f"{result:.2f}")