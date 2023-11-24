import heapq

N, M, A, B, C = map(int, input().split())
INF = 0x7F7F7F7F
d = [INF] * (N + 1)  # d[i] : i번 지점까지의 intensity
adj = [[] for _ in range(N + 1)]  # 간선(비용, 번호)


for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    adj[v].append((w, u))

heap = []
d[A] = 0
heapq.heappush(heap, (0, 0, A))

while heap:
    max_cost, total_cost, index = heapq.heappop(heap)
    if d[index] != max_cost:
        continue
    for nxt in adj[index]:
        if d[nxt[1]] <= max(d[index], nxt[0]):
            continue

        nxt_total_cost = total_cost + nxt[0]
        if nxt_total_cost <= C:
            d[nxt[1]] = max(d[index], nxt[0])
            heapq.heappush(heap, (d[nxt[1]], nxt_total_cost, nxt[1]))

print(d[B] if d[B] != INF else -1)
