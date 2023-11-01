from collections import defaultdict


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b, cnt):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]
    print(cnt[a])


for _ in range(int(input())):
    n = int(input())
    infos = [input().rstrip().split() for _ in range(n)]
    parents = defaultdict(str)
    cnt = defaultdict(int)
    for a, b in infos:
        if not parents[a]:
            parents[a] = a
            cnt[a] = 1
        if not parents[b]:
            parents[b] = b
            cnt[b] = 1
        union_parent(parents, a, b, cnt)
