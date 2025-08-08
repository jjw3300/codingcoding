T = int(input())

for i in range(1, T+1):
    n = int(input())
    number = list(map(int, input().split()))

    min_number = number[0]
    max_number = number[0]

    for j in number:
        if j < min_number:
            min_number = j

    for j in number:
        if j > max_number:
            max_number = j

    print(f'#{i} {max_number - min_number}')
