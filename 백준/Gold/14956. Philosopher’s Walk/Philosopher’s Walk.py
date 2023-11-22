def solve(M, K):
    if K == 1:
        if M == 0:
            return (1, 1)
        elif M == 1:
            return (1, 2)
        elif M == 2:
            return (2, 2)
        elif M == 3:
            return (2, 1)
    p2 = 1 << K
    square = M // (1 << (2 * K - 2))
    coor = solve(M - square * (1 << (2 * K - 2)), K - 1)
    if square == 0:
        return (coor[1], coor[0])
    elif square == 1:
        return (coor[0], coor[1] + p2 // 2)
    elif square == 2:
        return (coor[0] + p2 // 2, coor[1] + p2 // 2)
    return (p2 + 1 - coor[1], p2 // 2 + 1 - coor[0])


N, M = map(int, input().split())
K = 1
while 1 << K != N:
    K += 1
M -= 1
ans = solve(M, K)
print(ans[0], ans[1])
