T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, input().split())))
    max_kill = 0

    for a in range(n - m + 1):
        for b in range(n - m + 1):
            kill = 0
            for c in range(m):
                for d in range(m):
                    kill += area[a + c][b + d]
                    if kill > max_kill:
                        max_kill = kill

    print(f'#{i} {max_kill}')
