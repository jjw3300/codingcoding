T = 10
for tc in range(1, T + 1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    stalemate = 0
    for i in range(100):
        for j in range(100):
            if table[i][j] == 1:
                table[i][j] = 0
                for k in range(i, 100):
                    if table[k][j] == 1:
                        table[k][j] = 0
                    elif table[k][j] == 2:
                        table[k][j] = 0
                        stalemate += 1
                        break
    print(f"#{tc} {stalemate}")
