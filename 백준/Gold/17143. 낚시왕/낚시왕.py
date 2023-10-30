import sys
from copy import deepcopy
from collections import defaultdict

input = sys.stdin.readline


def get_shark(column):
    for i in range(R):
        number = board[i][column]
        if number:
            board[i][column] = 0
            return shark[number][2]
    return 0


def shark_move(x, y):
    number = board[x][y]
    s, d, z = shark[number]
    board[x][y] = 0

    if d == 1:
        if s <= x:
            x = x - s
        elif x < s <= x + (R - 1):
            x = s - x
            shark[number][1] = 2
        else:
            x = (R - 1) - (s - (x + R - 1))

    elif d == 2:
        if s <= (R - 1) - x:
            x = x + s
        elif (R - 1) - x < s <= 2 * (R - 1) - x:
            x = (R - 1) - (s - (R - 1 - x))
            shark[number][1] = 1
        else:
            x = s - (R - 1 - x + R - 1)

    elif d == 3:
        s = s % (2 * (C - 1))
        if s <= (C - 1) - y:
            y = y + s
        elif (C - 1) - y < s <= 2 * (C - 1) - y:
            y = (C - 1) - (s - (C - 1 - y))
            shark[number][1] = 4
        else:
            y = s - (C - 1 - y + C - 1)

    elif d == 4:
        if s <= y:
            y = y - s
        elif y < s <= y + (C - 1):
            y = s - y
            shark[number][1] = 3
        else:
            y = (C - 1) - (s - (y + C - 1))

    if new_board[x][y]:
        cur_size = shark[new_board[x][y]][2]
        if z > cur_size:
            new_board[x][y] = number
    else:
        new_board[x][y] = number


R, C, M = map(int, input().split())
dx, dy = (0, -1, 1, 0, 0), (0, 0, 0, 1, -1)
board = [[0] * C for _ in range(R)]
shark = [[0, 0, 0]]
ans = 0
for i in range(1, M + 1):
    r, c, s, d, z = map(int, input().split())
    if d == 1 or d == 2:
        s = s % (2 * (R - 1))
    else:
        s = s % (2 * (C - 1))
    board[r - 1][c - 1] = i
    shark.append([s, d, z])


for i in range(C):
    # 상어 잡기
    ans += get_shark(i)
    # 상어 이동
    new_board = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y]:
                shark_move(x, y)
    board = deepcopy(new_board)

print(ans)
