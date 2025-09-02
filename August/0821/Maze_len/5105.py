from collections import deque


def bfs(start, N):
    queue = deque([start])
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while True:
        if len(queue) == 0:
            break

        locate = queue.popleft()
        for a, b in delta:
            if 0 <= locate[0] + a < N and 0 <= locate[1] + b < N:

                if maze[locate[0] + a][locate[1] + b] == 3:
                    return maze[locate[0]][locate[1]] - 4

                if maze[locate[0] + a][locate[1] + b] == 0:
                    maze[locate[0] + a][locate[1] + b] = maze[locate[0]][locate[1]] + 1
                    queue.append([locate[0] + a, locate[1] + b])
    return 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                maze[i][j] = 4
                start_locate = [i, j]
                break

    print(f'#{tc} {bfs(start_locate, n)}')
