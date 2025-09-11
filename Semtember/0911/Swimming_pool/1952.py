T = int(input())
for tc in range(1, T + 1):
    ticket_price = list(map(int, input().split()))
    swimming_plan = list(map(int, input().split()))

    dp = [0] * 13

    for i in range(1, 13):
        dp[i] = min(dp[i - 1] + swimming_plan[i - 1] * ticket_price[0], dp[i - 1] + ticket_price[1])
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + ticket_price[2])
        else:
            dp[i] = min(dp[i], ticket_price[2])

    min_cost = min(dp[12], ticket_price[3])
    print(f"#{tc} {min_cost}")
