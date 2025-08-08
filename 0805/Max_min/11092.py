T = int(input())
for i in range(1, T + 1):
    n = int(input())
    number_list = list(map(int, input().split()))


    def max_locate(a):
        max_number = a[0]
        count = 0
        location = 0
        for num in a:
            if num >= max_number:
                max_number = num
                location = count
            count += 1
        return location

    def min_locate(a):
        min_number = a[0]
        count = 0
        location = 0
        for num in a:
            if num < min_number:
                min_number = num
                location = count
            count += 1
        return location


    answer = abs(max_locate(number_list) - min_locate(number_list))
    print(f"#{i} {answer}")
