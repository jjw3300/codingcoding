T = int(input())

for i in range(1, T+1):
    n = int(input())  # 방의 가로 길이
    box_list = list(map(int, input().split()))  # 상자의 수

    count = n
    box_count = 0
    drop_list = []

    for j in box_list:
        for k in range(0, len(box_list)):
            if j <= box_list[k]:
                box_count += 1
        drop_list.append(count - box_count)
        count -= 1

    max_number = drop_list[0]
    for j in drop_list:
        if max_number < j:
            max_number = j

    print(f'#{i} {max_number}')
