from collections import deque


def bfs(x, y, time, n, m, underground, locate):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((x, y, 1))
    visited[x][y] = True
    locate[x][y] = 1

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    tunnel_dir = {1: [0, 1, 2, 3],
                  2: [0, 2],
                  3: [1, 3],
                  4: [0, 1],
                  5: [1, 2],
                  6: [2, 3],
                  7: [0, 3]}
    connect = {0: [1, 2, 5, 6],
               1: [1, 3, 6, 7],
               2: [1, 2, 4, 7],
               3: [1, 3, 4, 5]}

    while queue:
        temp_x, temp_y, temp_time = queue.popleft()
        if temp_time >= time:
            continue

        for d in tunnel_dir[underground[temp_x][temp_y]]:
            nx, ny = temp_x + directions[d][0], temp_y + directions[d][1]
            if 0 <= nx < n and 0 <= ny < m:
                if underground[nx][ny] != 0 and not visited[nx][ny]:
                    if underground[nx][ny] in connect[d]:
                        visited[nx][ny] = 1
                        locate[nx][ny] = 1
                        queue.append((nx, ny, temp_time + 1))


T = int(input())
for tc in range(1, T + 1):
    n, m, x, y, time = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(n)]
    locate = [[0 for _ in range(m)] for _ in range(n)]

    bfs(x, y, time, n, m, underground, locate)

    count = 0
    for i in range(n):
        for j in range(m):
            if locate[i][j] == 1:
                count += 1
    print(f"#{tc} {count}")
