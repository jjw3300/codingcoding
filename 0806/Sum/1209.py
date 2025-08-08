T = 10

for i in range(1, T+1):
    n = int(input())

    main_area = []
    for j in range(100):
        main_area.append(list(map(int, input().split())))

    max_number = 0
    for x in range(100):
        sum_number = 0
        for y in range(100):
            sum_number += main_area[x][y]
        if max_number < sum_number:
            max_number = sum_number

        sum_number = 0
        for y in range(100):
            sum_number += main_area[y][x]
        if max_number < sum_number:
            max_number = sum_number

    sum_number = 0
    for x in range(100):
        sum_number += main_area[x][x]
    if max_number < sum_number:
        max_number = sum_number

    sum_number = 0
    for x in range(100):
        sum_number += main_area[x][99 - x]
    if max_number < sum_number:
        max_number = sum_number

    print(f'#{i} {max_number}')
