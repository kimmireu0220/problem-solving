from collections import defaultdict


n = int(input())
lst = list(map(int, input().split()))
sorted_list = sorted(set(lst))
result = defaultdict(int)
cnt = 0

for i in sorted_list:
    result[i] = cnt
    cnt += 1

answer = []
for i in lst:
    answer.append(result[i])

print(*answer)
