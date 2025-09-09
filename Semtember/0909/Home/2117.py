from collections import deque


def bfs(I, J, K):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque([(I, J, 0)])
    visited[I][J] = 1
    count = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        x, y, d = queue.popleft()
        if city[x][y] == 1:
            count += 1

        if d == K - 1:
            continue

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, d + 1))

    return count


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, n + 2):
                cost = k * k + (k - 1) * (k - 1)
                profit = bfs(i, j, k)
                if profit * m >= cost:
                    answer = max(answer, profit)

    print(f"#{tc} {answer}")
