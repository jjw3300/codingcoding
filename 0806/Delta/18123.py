T = int(input())

for i in range(1, T+1):
    n = int(input())

    area = []
    for _ in range(n):
        area.append(list(map(int, input().split())))

    num_abs = 0

    for x in range(n):
        for y in range(n):
            if x - 1 >= 0:
                num_abs += abs(area[x-1][y] - area[x][y])
            if y - 1 >= 0:
                num_abs += abs(area[x][y-1] - area[x][y])
            if x + 1 <= n - 1:
                num_abs += abs(area[x+1][y] - area[x][y])
            if y + 1 <= n - 1:
                num_abs += abs(area[x][y+1] - area[x][y])

    print(f'#{i} {num_abs}')
