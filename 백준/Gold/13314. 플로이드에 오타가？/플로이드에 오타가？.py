def solve():
    n = 100
    print(n)
    for y in range(n):
        for x in range(n):
            if x == y:
                print(0, end=' ')
            elif y == n - 1 or x == n - 1:
                print(4999, end=' ')
            else:
                print(10000, end=' ')
        print()

# solve 함수 호출
solve()
