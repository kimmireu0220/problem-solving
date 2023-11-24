def print_course(start, end):
    result = [start]
    while nxt[start][end] != end:
        result.append(nxt[start][end])
        start = nxt[start][end]
    result.append(end)
    return result


n = int(input())
m = int(input())
INF = 0x7F7F7F7F
board = [[INF] * (n + 1) for _ in range(n + 1)]
nxt = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    board[a][b] = min(board[a][b], cost)
    nxt[a][b] = b

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                temp = board[a][k] + board[k][b]
                if board[a][b] > temp:
                    board[a][b] = temp
                    nxt[a][b] = nxt[a][k]


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == INF:
            board[i][j] = 0

for i in board[1:]:
    print(*i[1:])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j]:
            temp = print_course(i, j)
            print(len(temp), *temp)
        else:
            print(0)
