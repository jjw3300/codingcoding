T = int(input())
for i in range(1, T + 1):
    n = int(input())

    main_area = []
    for j in range(10):
        main_area.append([0 for k in range(10)])

    color_area = []
    for j in range(n):
        color_area.append(list(map(int, input().split())))

    for j in color_area:
        if j[4] == 1:
            for x in range(j[0], j[2]+1):
                for y in range(j[1], j[3]+1):
                    if main_area[x][y] == 0:
                        main_area[x][y] = 1
                    elif main_area[x][y] == 2:
                        main_area[x][y] = 3

        if j[4] == 2:
            for x in range(j[0], j[2] + 1):
                for y in range(j[1], j[3] + 1):
                    if main_area[x][y] == 0:
                        main_area[x][y] = 2
                    elif main_area[x][y] == 1:
                        main_area[x][y] = 3

    count = 0
    for j in main_area:
        for k in j:
            if k == 3:
                count += 1

    print(f"#{i} {count}")
