T = int(input())

for i in range(1, T+1):

    area = []
    for _ in range(9):
        area.append(list(map(int, input().split())))

    dup_num = []
    possible = True
    for a in range(9):
        for b in range(9):
            if area[a][b] not in dup_num:
                dup_num.append(area[a][b])
            elif area[a][b] in dup_num:
                possible = False
        dup_num = []

    for a in range(9):
        for b in range(9):
            if area[b][a] not in dup_num:
                dup_num.append(area[b][a])
            elif area[b][a] in dup_num:
                possible = False
        dup_num = []

    for a in range(3):
        for b in range(3):
            dup_num = []
            for x in range(3):
                for y in range(3):
                    if area[a*3 + x][b*3 + y] not in dup_num:
                        dup_num.append(area[a*3 + x][b*3 + y])
                    elif area[a*3 + x][b*3 + y] in dup_num:
                        possible = False

    if possible is True:
        print(f'#{i} {1}')
    elif possible is False:
        print(f'#{i} {0}')
