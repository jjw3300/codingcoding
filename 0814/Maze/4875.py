def dfs(input_row, input_column):
    for i in delta:
        x, y = input_row + i[0], input_column + i[1]
        if 0 <= x < n and 0 <= y < n:
            if maze[x][y] == 3:
                return True
            elif maze[x][y] == 0:
                maze[x][y] = 2
                if dfs(x, y):
                    return True
    return False


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())
for tc in range(1, T + 1):
    n = int(input().strip())
    maze = [list(map(int, input().strip())) for _ in range(n)]

    start = []
    for row in range(n):
        for column in range(n):
            if maze[row][column] == 2:
                start.append(row)
                start.append(column)
                break
        if start:
            break

    escape = dfs(start[0], start[1])
    if escape:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
