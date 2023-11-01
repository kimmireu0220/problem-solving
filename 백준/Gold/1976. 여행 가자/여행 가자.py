def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))
parents = [i for i in range(N + 1)]
for i in range(N):
    for j in range(N):
        if board[i][j]:
            union_parent(parents, i + 1, j + 1)
result = [parents[plan] for plan in plans]
print("YES" if len(set(result)) == 1 else "NO")
