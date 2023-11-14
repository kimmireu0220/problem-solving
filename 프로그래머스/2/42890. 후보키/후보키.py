from itertools import combinations

def is_unique(rows, col_indexes):
    values_set = set()
    for row in rows:
        values = tuple(row[i] for i in col_indexes)
        if values in values_set:
            return False
        values_set.add(values)
    return True

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    candidate_keys = []

    for i in range(1, cols + 1):
        for comb in combinations(range(cols), i):
            if is_unique(relation, comb):
                is_minimal = True
                for key in candidate_keys:
                    if set(key).issubset(set(comb)):
                        is_minimal = False
                        break
                if is_minimal:
                    candidate_keys.append(comb)

    return len(candidate_keys)

# Example usage
relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"]
]

result = solution(relation)
print(result)  # Output: 2
