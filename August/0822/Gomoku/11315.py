T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    gomoku = [list(map(str, input())) for _ in range(n)]
    win = False

    count = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if gomoku[i][j] == 'o':
                count += 1
                if count >= 5:
                    win = True
                    break
            elif gomoku[i][j] == '.':
                count = 0
        if win:
            break

    for j in range(n):
        count = 0
        for i in range(n):
            if gomoku[i][j] == 'o':
                count += 1
                if count >= 5:
                    win = True
                    break
            elif gomoku[i][j] == '.':
                count = 0
        if win:
            break

    for i in range(n - 4):
        for j in (range(n - 4)):
            count = 0
            for k in range(5):
                if gomoku[i + k][j + k] == 'o':
                    count += 1
                else:
                    break
            if count == 5:
                win = True
                break
        if win:
            break

    for i in range(n - 4):
        for j in range(4, n):
            count = 0
            for k in range(5):
                if gomoku[i + k][j - k] == 'o':
                    count += 1
                else:
                    break
            if count == 5:
                win = True
                break
        if win:
            break

    if win:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')