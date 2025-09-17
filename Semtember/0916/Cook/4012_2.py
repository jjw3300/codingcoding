def make_combinations(arr, r):
    result = []

    def dfs(start, temp):
        if len(temp) == r:
            result.append(temp[:])
            return

        for i in range(start, len(arr)):
            temp.append(arr[i])
            dfs(i + 1, temp)
            temp.pop()

    dfs(0, [])
    return result


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]

    min_gap = float('inf')
    food = set(range(n))

    for food1 in make_combinations(list(food), n // 2):
        food2 = list(food - set(food1))
        food1 = list(food1)

        food1_synergy = 0
        for a in range(len(food1)):
            for b in range(a + 1, len(food1)):
                i = food1[a]
                j = food1[b]
                food1_synergy += synergy[i][j] + synergy[j][i]

        food2_synergy = 0
        for a in range(len(food2)):
            for b in range(a + 1, len(food2)):
                i = food2[a]
                j = food2[b]
                food2_synergy += synergy[i][j] + synergy[j][i]

        gap = abs(food1_synergy - food2_synergy)
        if gap < min_gap:
            min_gap = gap

    print(f"#{tc} {min_gap}")
