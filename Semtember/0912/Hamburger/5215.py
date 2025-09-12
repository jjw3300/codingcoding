T = int(input())
for tc in range(1, T + 1):
    topping, max_cal = map(int, input().split())
    topping_list = [list(map(int, input().split())) for _ in range(topping)]

    dp = [0] * (max_cal + 1)

    for taste, cal in topping_list:
        for i in range(max_cal, cal - 1, -1):
            dp[i] = max(dp[i], dp[i - cal] + taste)

    max_taste = max(dp)
    print(f"#{tc} {max_taste}")
