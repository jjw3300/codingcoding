def backtracking(row, percent):
    global max_percent

    if row == n:
        max_percent = max(max_percent, percent)
        return

    if percent <= max_percent:
        return

    for col in range(n):
        if not visited[col]:
            visited[col] = 1
            backtracking(row + 1, percent * (success[row][col] / 100))
            visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    success = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    max_percent = 0

    backtracking(0, 1)
    print(f"#{tc} {round(max_percent * 100, 6):.6f}")
