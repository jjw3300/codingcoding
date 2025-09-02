T = int(input())

for tc in range(1, T+1):
    n = str(input())
    if n == n[::-1]:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
