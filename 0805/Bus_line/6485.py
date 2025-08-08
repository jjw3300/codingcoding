T = int(input())
for i in range(1, T + 1):
    n = int(input())
    bus_line = []
    for j in range(1, n+1):
        bus_line.append(list(map(int, input().split())))

    p = int(input())
    main_line = []
    for _ in range(p):
        main_line.append(int(input()))

    count_line = []
    for _ in range(p):
        count_line.append(0)

    for j in range(p):
        station = main_line[j]
        for k in bus_line:
            if k[0] <= station <= k[1]:
                count_line[j] += 1

    print(f"#{i}", *count_line)
