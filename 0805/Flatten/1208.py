T = 10
for i in range(1, T + 1):
    dump = int(input())
    box_list = list(map(int, input().split()))

    def max_num(a):
        max_number = a[0]
        count = 0
        location = 0
        for num in a:
            if num > max_number:
                max_number = num
                location = count
            count += 1
        return [max_number, location]

    def min_num(a):
        min_number = a[0]
        count = 0
        location = 0
        for num in a:
            if num < min_number:
                min_number = num
                location = count
            count += 1
        return [min_number, location]

    for j in range(dump):
        box_list[max_num(box_list)[1]], box_list[min_num(box_list)[1]] \
            = (box_list[max_num(box_list)[1]] - 1), (box_list[min_num(box_list)[1]] + 1)

    answer = max_num(box_list)[0] - min_num(box_list)[0]

    print(f"#{i} {answer}")
