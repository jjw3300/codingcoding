T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = board[0][0]

    for x in range(1, n):
        dp[x][0] = dp[x - 1][0] + board[x][0]
    for y in range(1, n):
        dp[0][y] = dp[0][y - 1] + board[0][y]

    for x in range(1, n):
        for y in range(1, n):
            dp[x][y] = board[x][y] + min(dp[x - 1][y], dp[x][y - 1])

    print(f"#{tc} {dp[n - 1][n - 1]}")
