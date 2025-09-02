T = int(input())
for i in range(1, T + 1):
    n = int(input())
    cards_list = list(map(int, input()))

    max_number = [[0] for _ in range(10)]

    for j in cards_list:
        max_number[j][0] += 1

    max_num = max_number[0]
    count = 0
    max_count = 0

    for j in max_number:
        if max_num <= j:
            max_num = j
            max_count = count
        count += 1

    print(f"#{i} {max_count} {max_num[0]}")
