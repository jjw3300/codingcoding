T = int(input())

for i in range(1, T+1):
    n = int(input())
    area = list(map(int, input().split()))
    max_list = []

    number = area[0]
    count = 1
    for j in area:
        if number < j:
            count += 1
            number = j
            max_list.append(count)
        else:
            count = 1
            number = j
        max_list.append(count)

    max_num = max_list[0]
    for j in max_list:
        if max_num < j:
            max_num = j

    print(f'#{i} {max_num}')
