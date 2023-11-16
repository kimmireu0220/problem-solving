from collections import deque


def get_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def solution(n, m, x, y, r, c, k):
    x, y = y - 1, x - 1
    r, c = r - 1, c - 1

    def bfs():
        q = deque([(x, y, "")])
        visited = set()
        visited.add((x, y))
        while q:
            x1, y1, path = q.popleft()
            if x1 == c and y1 == r:
                return path

            for i in range(4):
                nx = x1 + dx[i]
                ny = y1 + dy[i]
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                q.append((nx, ny, path + path_map[i]))

    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]

    path_map = {0: "d", 1: "l", 2: "r", 3: "u"}

    diff = k
    answer = ""
    while diff:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if get_dist(nx, ny, c, r) <= diff:
                answer += path_map[i]
                x, y = nx, ny
                diff -= 1
                break
        else:
            break

    if len(answer) == k and x == c and y == r:
        return answer
    return "impossible"
