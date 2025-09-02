T = int(input())

for i in range(1, T + 1):
    n = input()
    m = input()

    if n in m:
        print(f'#{i} {1}')
    else:
        print(f'#{i} {0}')
