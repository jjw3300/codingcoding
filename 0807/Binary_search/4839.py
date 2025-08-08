T = int(input())

for i in range(1, T+1):
    book, a, b = map(int, input().split())
    a_count = 0
    b_count = 0

    start = 1
    end = book
    middle = (start + end) // 2
    while a != middle:
        middle = (start + end) // 2
        if a == middle:
            break
        elif a > middle:
            a_count += 1
            start = (start + end) // 2
        elif a < middle:
            a_count += 1
            end = (start + end) // 2

    start = 1
    end = book
    middle = (start + end) // 2
    while b != middle:
        middle = (start + end) // 2
        if b == middle:
            break
        elif b > middle:
            b_count += 1
            start = (start + end) // 2
        elif b < middle:
            b_count += 1
            end = (start + end) // 2

    if a_count < b_count:
        print(f'#{i} A')
    elif a_count > b_count:
        print(f'#{i} B')
    else:
        print(f'#{i} {0}')
