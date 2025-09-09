T = int(input())
for tc in range(1, T + 1):
    n, high = map(int, input().split())
    staff = list(map(int, input().split()))
    answer = float('inf')

    for i in range(1 << n):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += staff[j]
        if subset_sum - high >= 0:
            answer = min(answer, subset_sum - high)

    print(f"#{tc} {answer}")
