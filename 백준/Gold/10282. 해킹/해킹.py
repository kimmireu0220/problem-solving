import heapq


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    cnt = 1

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for index, cost in graph[now]:
            new_cost = dist + cost
            if distance[index] > new_cost:
                if distance[index] == INF:
                    cnt += 1
                distance[index] = new_cost
                heapq.heappush(queue, (new_cost, index))
    max_distance = max([i for i in distance if i != INF])
    return cnt, max_distance


INF = int(1e9)
for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, cost = map(int, input().split())
        graph[b].append((a, cost))
    print(*dijkstra(c))
