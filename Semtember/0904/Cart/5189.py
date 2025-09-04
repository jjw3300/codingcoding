from itertools import permutations

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    number = [i for i in range(2, n + 1)]
    battery = []
    for i in permutations(number, n - 1):
        before_num = 1
        temp = 0
        for j in i:
            temp += board[before_num - 1][j - 1]
            before_num = j
        temp += board[before_num - 1][0]
        battery.append(temp)

    print(f"#{tc} {min(battery)}")
