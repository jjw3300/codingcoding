T = int(input())
for tc in range(1, T + 1):
    delta = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m, k = map(int, input().split())
    cell = [[[] for _ in range(n)] for _ in range(n)]

    for _ in range(k):
        x, y, number, direction = map(int, input().split())
        cell[x][y].append([number, direction])

    for _ in range(m):
        new_cell = [[[] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if len(cell[i][j]) > 0:
                    num, dire = cell[i][j][0]
                    dx = i + delta[dire][0]
                    dy = j + delta[dire][1]
                    if dx == 0 or dx == n - 1 or dy == 0 or dy == n - 1:
                        num = num // 2
                        if num == 0:
                            continue
                        if dire == 1:
                            dire = 2
                        elif dire == 2:
                            dire = 1
                        elif dire == 3:
                            dire = 4
                        elif dire == 4:
                            dire = 3
                    new_cell[dx][dy].append([num, dire])

        for i in range(n):
            for j in range(n):
                if len(new_cell[i][j]) > 1:
                    total = 0
                    max_group = new_cell[i][j][0]
                    for group in new_cell[i][j]:
                        total += group[0]
                        if group[0] > max_group[0]:
                            max_group = group
                    max_num, max_dire = max_group
                    new_cell[i][j] = [[total, max_dire]]

        cell = new_cell

    count = 0
    for i in range(n):
        for j in range(n):
            if len(cell[i][j]) > 0:
                count += cell[i][j][0][0]

    print(f"#{tc} {count}")
