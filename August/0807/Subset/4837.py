T = int(input())
for i in range(1, T + 1):
    n, k = map(int, input().split())

    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0

    for a in range(1 << len(number_list)):
        set_num = []
        for b in range(len(number_list)):
            if a & (1 << b):
                set_num.append(number_list[b])

        sum_num = 0
        for b in set_num:
            sum_num += b

        if len(set_num) == n and sum_num == k:
            count += 1

    print(f"#{i} {count}")
