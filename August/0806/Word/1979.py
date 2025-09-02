T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, input().split())))

    count = 0
    possible_count = 0
    for a in range(n):
        for b in range(n):
            if area[a][b] == 1:
                count += 1
            else:
                if count == k:
                    possible_count += 1
                count = 0
        if count == k:
            possible_count += 1
        count = 0

    for a in range(n):
        for b in range(n):
            if area[b][a] == 1:
                count += 1
            else:
                if count == k:
                    possible_count += 1
                count = 0
        if count == k:
            possible_count += 1
        count = 0

    print(f'#{i} {possible_count}')
