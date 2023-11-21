import sys

input = sys.stdin.readline


def check_board():
    temp = []
    for i in range(n):
        for j in range(m):
            if board[i][j] and board[i][j] != 6:
                temp.append([i, j])
    return temp


def get_blank():
    temp = 0
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                temp += 1
    return temp


def dfs(idx):
    global ans
    if idx == cctv_len:
        temp = get_blank()
        if ans > temp:
            ans = temp
        return

    x, y = cctv_lst[idx]
    number = board[x][y]
    cctv = cctvs[number]

    for cv in cctv:
        temp_lst = []
        for num in cv:
            sx, sy = x, y
            dx, dy = move[num]
            while True:
                nx, ny = sx + dx, sy + dy
                if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 6:
                    break
                if not board[nx][ny]:
                    board[nx][ny] = number
                    temp_lst.append([nx, ny])
                sx, sy = nx, ny
        dfs(idx + 1)
        for a, b in temp_lst:
            board[a][b] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = n * m
cctvs = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],
]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cctv_lst = check_board()
cctv_len = len(cctv_lst)
dfs(0)
print(ans)
