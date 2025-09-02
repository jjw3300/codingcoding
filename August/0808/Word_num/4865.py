T = int(input())

for i in range(1, T+1):
    n = input()
    m = input()
    max_count = -1
    for j in n:
        count = 0
        for k in m:
            if j == k:
                count += 1
            if max_count < count:
                max_count = count

    print(f'#{i} {max_count}')
