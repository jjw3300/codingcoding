from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    pool = [list(input()) for _ in range(n)]
    distance = [[-1] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if pool[i][j] == 'W':
                q.append((i, j))
                distance[i][j] = 0

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for a, b in delta:
            dx, dy = x + a, y + b
            if 0 <= dx < n and 0 <= dy < m and distance[dx][dy] == -1:
                distance[dx][dy] = distance[x][y] + 1
                q.append((dx, dy))

    answer = 0
    for i in range(n):
        for j in range(m):
            if pool[i][j] == 'L':
                answer += distance[i][j]

    print(f'#{tc} {answer}')
