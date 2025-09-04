def dfs(x, y, start_x, start_y, visited_cafe, direction, turn_count):
    global max_desserts

    possible_direction = [direction, direction + 1]
    for d in possible_direction:
        if d > 3:
            continue

        dx, dy = x + delta[d][0], y + delta[d][1]
        if 0 <= dx < n and 0 <= dy < n:
            if dx == start_x and dy == start_y and len(visited_cafe) >= 4:
                max_desserts = max(max_desserts, len(visited_cafe))
                continue

            if dessert_cafe[dx][dy] not in visited_cafe:
                visited_cafe.append(dessert_cafe[dx][dy])

                temp_count = turn_count
                if d != direction:
                    temp_count += 1
                dfs(dx, dy, start_x, start_y, visited_cafe, d, temp_count)

                visited_cafe.pop()


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    dessert_cafe = [list(map(int, input().split())) for _ in range(n)]
    max_desserts = -1
    delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    for i in range(n):
        for j in range(n):
            for start_direction in range(4):
                dfs(i, j, i, j, [dessert_cafe[i][j]], start_direction, 0)

    print(f"#{tc} {max_desserts}")
