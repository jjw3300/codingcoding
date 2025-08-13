T = int(input())
delta = [[1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0]]


for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(0 for _ in range(n)) for _ in range(n)]
    board_set = [n//2, n//2 - 1]
    for i in board_set:
        for j in board_set:
            if i == j:
                board[i][j] = 2
            else:
                board[i][j] = 1

    for i in range(m):
        a, b, stone = map(int, input().split())
        for x, y in delta:
            board[a - 1][b - 1] = stone
            need_change = []
            for c in range(1, n):
                ax = (a - 1) + (x * c)
                by = (b - 1) + (y * c)
                if 0 <= ax < n and 0 <= by < n:
                    if board[ax][by] == 0:
                        break
                    elif board[ax][by] != stone:
                        need_change.append([ax, by])
                    else:
                        for x_point, y_point in need_change:
                            board[x_point][y_point] = stone
                        break
                else:
                    break

    count_white = 0
    count_black = 0
    for i in board:
        for j in i:
            if j == 1:
                count_white += 1
            elif j == 2:
                count_black += 1

    print(f'#{tc} {count_white} {count_black}')
