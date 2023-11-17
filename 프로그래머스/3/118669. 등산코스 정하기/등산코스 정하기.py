

import heapq

MX = 0x7F7F7F7F
d = [MX] * 50005  # d[i] : i번 지점까지의 intensity
adj = [[] for _ in range(50005)]  # 간선(비용, 번호)
issummit = [False] * 50005  # issummit[i] : i번 지점이 summit인지 여부.


def solution(n, paths, gates, summits):
    for summit in summits:
        issummit[summit] = True
    for u, v, w in paths:
        adj[u].append((w, v))
        adj[v].append((w, u))
    heap = []
    for g in gates:
        d[g] = 0
        heapq.heappush(heap, (d[g], g))
    while heap:
        cost, index = heapq.heappop(heap)  # cost : 현재까지의 비용, index : 현재 보는 정점의 인덱스
        if d[index] < cost:
            continue
        for nxt in adj[index]:  # nxt[0] : 간선의 비용, nxt[1] : 간선이 연결하는 인덱스
            if d[nxt[1]] <= max(d[index], nxt[0]):
                continue
            d[nxt[1]] = max(d[index], nxt[0])
            if not issummit[nxt[1]]:
                heapq.heappush(heap, (d[nxt[1]], nxt[1]))

    ans = summits[0]
    for summit in summits:
        if d[summit] < d[ans]:
            ans = summit
        elif d[summit] == d[ans] and summit < ans:
            ans = summit
    return [ans, d[ans]]