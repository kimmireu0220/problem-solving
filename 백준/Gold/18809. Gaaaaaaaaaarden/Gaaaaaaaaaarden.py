from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

input = sys.stdin.readline


def get_possible_points():
    result = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                result.append([i, j])
    return result


def solve(green, red):
    new_board = deepcopy(board)
    q = deque()
    cnt = 0
    for a, b in green:
        new_board[a][b] = 3
        q.append([a, b, 3])
    for a, b in red:
        new_board[a][b] = 4
        q.append([a, b, 4])
    while q:
        temp = []
        for _ in range(len(q)):
            x, y, flag = q.popleft()
            if new_board[x][y] == 7:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    not (0 <= nx < N and 0 <= ny < M)
                    or new_board[x][y] == new_board[nx][ny]
                    or new_board[nx][ny] == 0
                ):
                    continue
                if new_board[nx][ny] == 1 or new_board[nx][ny] == 2:
                    new_board[nx][ny] = flag
                    q.append([nx, ny, flag])
                    temp.append([nx, ny])
                elif new_board[nx][ny] == 3 or new_board[nx][ny] == 4:
                    if [nx, ny] in temp:
                        new_board[nx][ny] = 7
                        cnt += 1
    return cnt


N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
possible_points = get_possible_points()
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
answer = 0
for possible_point in combinations(possible_points, G + R):
    greens = combinations(possible_point, G)
    for green in greens:
        red = [i for i in possible_point if i not in green]
        temp = solve(green, red)
        if answer < temp:
            answer = temp
print(answer)
