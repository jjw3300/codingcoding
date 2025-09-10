from collections import deque


def bfs(temp_x, temp_y, temp_number):
    queue = deque()
    queue.append((temp_x, temp_y, temp_number))

    while queue:
        x, y, number = queue.popleft()
        if len(number) == 7:
            numbers_set.add(''.join(number))
        else:
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    queue.append((nx, ny, number + [board[nx][ny]]))


T = int(input())
for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    numbers_set = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j, [board[i][j]])

    print(f"#{tc} {len(numbers_set)}")
