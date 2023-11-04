from heapq import heappop, heappush


numbers = [int(input()) for _ in range(int(input()))]

if len(numbers) == 1:
    print(numbers[0])
else:
    left, right = [-min(numbers[0], numbers[1])], [max(numbers[0], numbers[1])]
    print(numbers[0])
    print(-left[0])

    for idx, val in enumerate(numbers[2:], start=2):
        if idx % 2:
            max_left = -heappop(left)
            if val > max_left:
                heappush(left, -max_left)
                heappush(right, val)
            else:
                heappush(left, -val)
                heappush(right, max_left)
        else:
            min_right = heappop(right)
            if val > min_right:
                heappush(left, -min_right)
                heappush(right, val)
            else:
                heappush(left, -val)
                heappush(right, min_right) 
        print(-left[0])
