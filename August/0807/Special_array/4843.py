T = int(input())

for i in range(1, T+1):
    def max_list(a, b):
        for j in range(b - 1):
            min_idx = j
            for k in range(j + 1, b):
                if a[min_idx] > a[k]:
                    min_idx = k
            a[j], a[min_idx] = a[min_idx], a[j]
        return a


    n = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = max_list(num_list, n)

    count = 0
    first_list = []
    second_list = []
    new_list = []

    for number in sorted_list:
        if count >= len(sorted_list) // 2:
            second_list.append(number)
            count += 1
        else:
            first_list.append(number)
            count += 1

    second_list = second_list[::-1]

    for num in range(n//2):
        new_list.append(second_list[num])
        new_list.append(first_list[num])

    new_list = new_list[:10]
    print(f'#{i}', *new_list)
