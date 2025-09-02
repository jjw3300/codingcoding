T = int(input())

for i in range(1, T+1):
    n = int(input())
    number_list = list(input())

    count = 0
    one_list = [0]

    for j in number_list:
        if j == '0':
            one_list.append(count)
            count = 0
        elif j == '1':
            count += 1
            one_list.append(count)

    max_number = one_list[0]
    for j in one_list:
        if j > max_number:
            max_number = j

    print(f'#{i} {max_number}')
