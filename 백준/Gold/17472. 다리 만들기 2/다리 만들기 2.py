from collections import deque


def check_island_bfs(x, y, visited, group_number, groups):
    q = deque([[x, y]])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    groups[group_number].append([nx, ny])


def check_island():
    groups = [[] for _ in range(7)]
    group_number = 1
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j]:
                visited[i][j] = True
                groups[group_number].append([i, j])
                check_island_bfs(i, j, visited, group_number, groups)
                group_number += 1
    for i in range(1, 7):
        if groups[i]:
            for x, y in groups[i]:
                board[x][y] = i
    return groups, group_number - 1


def check_distance_bfs(x, y, number, edges, is_connected):
    for i in range(4):
        cx, cy = x, y
        cost = 0
        while True:
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                break
            temp_number = board[nx][ny]
            if temp_number == number:
                break
            else:
                if temp_number:
                    if cost >= 2:
                        edges.append([cost, number, temp_number])
                        is_connected[number].append(temp_number)
                        is_connected[temp_number].append(number)
                    break
                else:
                    cost += 1
                    cx, cy = nx, ny


def check_connected(is_connected, total_groups):
    q = deque([1])
    visited, visited[1] = [False] * (total_groups + 1), True
    while q:
        cur_node = q.popleft()
        for i in is_connected[cur_node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return True if not visited[1:].count(False) else False


def check_distance(groups, total_groups):
    edges = []
    is_connected = [[] for _ in range(total_groups + 1)]
    for i in range(1, total_groups + 1):
        for x, y in groups[i]:
            check_distance_bfs(x, y, i, edges, is_connected)
    return sorted(edges), check_connected(is_connected, total_groups)


def get_result(total_groups, edges):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(total_groups + 1)]
    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    return result


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
groups, total_groups = check_island()
edges, all_connected = check_distance(groups, total_groups)
result = get_result(total_groups, edges) if all_connected else -1
print(result)
