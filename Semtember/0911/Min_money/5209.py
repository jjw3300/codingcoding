def backtracking(row, money):
    global min_money

    if row == n:
        min_money = min(min_money, money)
        return

    if money >= min_money:
        return

    for col in range(n):
        if not visited[col]:
            visited[col] = 1
            backtracking(row + 1, money + success[row][col])
            visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    success = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_money = float('inf')

    backtracking(0, 0)
    print(f"#{tc} {min_money}")
