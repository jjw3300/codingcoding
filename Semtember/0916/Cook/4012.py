from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]

    min_gap = float('inf')
    food = set(range(n))

    for food1 in combinations(range(n), n // 2):
        food2 = list(food - set(food1))
        food1 = list(food1)

        food1_synergy = sum(synergy[i][j] + synergy[j][i] for i, j in combinations(food1, 2))
        food2_synergy = sum(synergy[i][j] + synergy[j][i] for i, j in combinations(food2, 2))

        gap = abs(food1_synergy - food2_synergy)
        if gap < min_gap:
            min_gap = gap

    print(f"#{tc} {min_gap}")
