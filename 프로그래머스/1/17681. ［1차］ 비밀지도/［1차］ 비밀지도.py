def solve(a, b, n):
    result = []
    for i in range(n):
        temp = ""
        for j in range(n):
            if a[i][j] == "1" or b[i][j] == "1":
                temp = temp + "#"
            else:
                temp = temp + " "
        result.append(temp)
    return result


def make_board(arr, n):
    board = []
    for i in arr:
        temp = bin(i)[2:].zfill(n)
        board.append(temp)
    return board


def solution(n, arr1, arr2):
    a, b = make_board(arr1, n), make_board(arr2, n)
    answer = solve(a, b, n)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
