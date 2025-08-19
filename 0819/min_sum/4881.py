def permutation(row, current_sum):
    global min_sum
    if current_sum >= min_sum:
        return

    if row == n:
        min_sum = min(min_sum, current_sum)
        return

    for col in range(n):
        if not visited[col]:
            visited[col] = True
            permutation(row + 1, current_sum + number_list[row][col])
            visited[col] = False


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    number_list = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * n
    min_sum = float("inf")

    permutation(0, 0)

    print(f"#{tc} {min_sum}")
