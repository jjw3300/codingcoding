T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, input().split())))

    max_answer = 0
    for a in range(n):
        for b in range(m):
            max_num = area[a][b]
            for j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if 0 <= a+j[0] < n and 0 <= b+j[1] < m:
                    max_num += area[a+j[0]][b+j[1]]
            if max_num > max_answer:
                max_answer = max_num

    print(f'#{i} {max_answer}')
