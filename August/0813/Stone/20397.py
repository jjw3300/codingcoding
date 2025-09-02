def change(num):
    if num == 1:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    stones = list(map(int, input().split()))
    order = []
    for a in range(m):
        order.append(list(map(int, input().split())))

    for a, b in order:
        for i in range(1, b + 1):
            if 0 <= (a - 1 - i) < n and 0 <= (a - 1 + i) < n:
                if stones[a - 1 + i] == stones[a - 1 - i]:
                    stones[a - 1 + i], stones[a - 1 - i]\
                        = change(stones[a - 1 + i]), change(stones[a - 1 - i])
            else:
                break

    print(f'#{tc}', *stones)
