T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    number_list = list(map(int, input().split()))

    sum_list = []
    for j in range(0, len(number_list) + 1 - m):
        sum_number = 0
        for k in range(m):
            sum_number += number_list[j+k]
        sum_list.append(sum_number)

    max_number = sum_list[0]
    min_number = sum_list[0]

    for j in sum_list:
        if max_number < j:
            max_number = j

    for j in sum_list:
        if min_number > j:
            min_number = j

    print(f'#{i} {max_number - min_number}')
