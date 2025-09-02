T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cube_root = round(n ** (1/3))

    if cube_root ** 3 != n:
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {cube_root}')
