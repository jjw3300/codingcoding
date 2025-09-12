T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    point = list(map(int, input().split()))
    dp = [0] * (sum(point) + 1)
    dp[0] = 1

    for i in point:
        for j in range(sum(point) - i, - 1, -1):
            if dp[j]:
                dp[j+i] = 1

    count = 0
    for i in dp:
        if i != 0:
            count += 1

    print(f"#{tc} {count}")
