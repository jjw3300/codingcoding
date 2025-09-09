delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y, length, dig):
    global max_length
    max_length = max(max_length, length)

    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0:
                if mountain[nx][ny] < mountain[x][y]:
                    visited[nx][ny] = 1
                    dfs(nx, ny, length + 1, dig)
                    visited[nx][ny] = 0
                elif not dig and mountain[nx][ny] - deep < mountain[x][y]:
                    temp = mountain[nx][ny]
                    mountain[nx][ny] = mountain[x][y] - 1
                    visited[nx][ny] = 1
                    dfs(nx, ny, length + 1, True)
                    visited[nx][ny] = 0
                    mountain[nx][ny] = temp


T = int(input())
for tc in range(1, T + 1):
    n, deep = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]

    max_height = 0
    for i in mountain:
        max_height = max(max_height, max(i))

    starts = []
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == max_height:
                starts.append((i, j))

    max_length = 0
    for sx, sy in starts:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[sx][sy] = 1
        dfs(sx, sy, 1, False)

    print(f"#{tc} {max_length}")
