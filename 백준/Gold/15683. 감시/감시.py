def get_cctvs():
    cctvs = []
    for i in range(n):
        for j in range(m):
            if board[i][j] and board[i][j] != 6:
                cctvs.append([i, j, board[i][j]])
    return cctvs, len(cctvs)


def get_blank(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                cnt += 1
    return cnt


def solve(case):
    def upd(x, y, direction):
        direction %= 4
        while True:
            x += dx[direction]
            y += dy[direction]
            if not (0 <= x < n and 0 <= y < m) or new_board[x][y] == 6:
                break
            new_board[x][y] = 7

    new_board = [[board[i][j] for j in range(m)] for i in range(n)]

    for i in range(cctvs_length):
        direction = case % 4
        x, y, cctv_type = cctvs[i]
        if cctv_type == 1:
            upd(x, y, direction)
        elif cctv_type == 2:
            upd(x, y, direction)
            upd(x, y, direction + 2)
        elif cctv_type == 3:
            upd(x, y, direction)
            upd(x, y, direction + 1)
        elif cctv_type == 4:
            upd(x, y, direction)
            upd(x, y, direction + 1)
            upd(x, y, direction + 2)
        else:
            upd(x, y, direction)
            upd(x, y, direction + 1)
            upd(x, y, direction + 2)
            upd(x, y, direction + 3)
        case //= 4
    return get_blank(new_board)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctvs, cctvs_length = get_cctvs()
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
answer = get_blank(board)

for case in range(4**cctvs_length):
    temp = solve(case)
    answer = min(answer, temp)

print(answer)
