from collections import deque


def direction(s):
    if s == "|":
        return [0, 1]
    elif s == "-":
        return [2, 3]
    elif s == "+" or s == "M" or s == "Z":
        return [0, 1, 2, 3]
    elif s == "1":
        return [1, 3]
    elif s == "2":
        return [0, 3]
    elif s == "3":
        return [0, 2]
    elif s == "4":
        return [1, 2]


def bfs(y, x, dir):
    global final_y, final_x
    q = deque()
    q.append([y, x, dir])
    check[y][x] = True
    while q:
        oy, ox, odir = q.popleft()
        # print(oy, ox, odir)
        for d in odir:
            ny = oy + dy[d]
            nx = ox + dx[d]
            nd = (d + 1) % 2 if d < 2 else (d + 1) % 2 + 2
            # 방문한 적이 없을 때
            if 0 <= ny < r and 0 <= nx < c and not check[ny][nx]:
                if europe[ny][nx] != ".":  # 가스관이 있는자리라면
                    check[ny][nx] = True  # 방문체크해주고
                    # 그 가스관의 가능한 방향 넣어준다
                    q.append([ny, nx, direction(europe[ny][nx])])
                else:  # 가스관이 없는 빈칸이라면
                    if europe[oy][ox] == "M" or europe[oy][ox] == "Z":
                        continue
                    final_y, final_x = ny, nx
                    # print(final_y, final_x)
                    if nd not in dir_candidate:
                        dir_candidate.append(nd)


r, c = map(int, input().split())
check = [[False] * (c) for _ in range(r)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

europe = []
for i in range(r):
    europe.append(list(input().strip()))
    for j in range(c):
        if europe[i][j] == "M":
            my, mx = i, j
        elif europe[i][j] == "Z":
            zy, zx = i, j
            # print(europe)
# print(my, mx, zy, zx)
dir_candidate, final_y, final_x = [], 0, 0
bfs(my, mx, [0, 1, 2, 3])
bfs(zy, zx, [0, 1, 2, 3])

# print(f'중간점검 {dir_candidate}, {final_y}, {final_x}')

for i in range(r):
    for j in range(c):
        if europe[i][j] != "." and not check[i][j]:
            bfs(i, j, direction(europe[i][j]))

dir_candidate.sort()

# print(f'최종점검 {dir_candidate}, {final_y}, {final_x}')

samples = ["|", "-", "+", "1", "2", "3", "4"]
for s in samples:
    if dir_candidate == direction(s):
        print(final_y + 1, final_x + 1, s)
