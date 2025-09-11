from collections import deque


def bfs(temp_x, temp_y, temp_count):
    global max_room, max_point

    queue = deque()
    queue.append((temp_x, temp_y, temp_count))

    while queue:
        x, y, count = queue.popleft()
        if max_room < count:
            max_room = count
            max_point = room[i][j]
        elif max_room == count:
            max_point = min(max_point, room[i][j])
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if int(room[x][y] + 1) == room[nx][ny]:
                    queue.append((nx, ny, count + 1))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    max_room = 0
    max_point = float('inf')
    for i in range(n):
        for j in range(n):
            bfs(i, j, 1)

    print(f"#{tc} {max_point} {max_room}")
