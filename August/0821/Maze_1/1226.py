from collections import deque


def bfs(x, y):
    N = 16
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if maze[x][y] == 3:
            return 1

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return 0


T = 10

for tc in range(1, T + 1):
    n = input()
    maze = [list(map(int, input().strip())) for _ in range(16)]
    start_x = start_y = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    print(f"#{tc} {bfs(start_x, start_y)}")
