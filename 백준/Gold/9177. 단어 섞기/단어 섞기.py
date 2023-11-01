from collections import deque


def solve(i, a, b, c):
    len_a, len_b, len_c = len(a), len(b), len(c)
    q = deque([[0, 0, 0]])
    visited = [[False] * (len_b + 1) for _ in range(len_a + 1)]
    visited[0][0] = True
    while q:
        a_idx, b_idx, c_idx = q.popleft()
        if c_idx == len_c:
            return f"Data set {i}: yes"
        a_letter = a[a_idx] if a_idx < len_a else None
        b_letter = b[b_idx] if b_idx < len_b else None
        c_letter = c[c_idx]
        if a_letter == c_letter:
            if not visited[a_idx + 1][b_idx]:
                visited[a_idx + 1][b_idx] = True
                q.append([a_idx + 1, b_idx, c_idx + 1])
        if b_letter == c_letter:
            if not visited[a_idx][b_idx + 1]:
                visited[a_idx][b_idx + 1] = True
                q.append([a_idx, b_idx + 1, c_idx + 1])
    return f"Data set {i}: no"


n = int(input())
for i in range(1, n + 1):
    a, b, c = list(input().rstrip().split())
    print(solve(i, a, b, c))
