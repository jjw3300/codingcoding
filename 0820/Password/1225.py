from collections import deque
T = 10
for tc in range(1, T + 1):
    n = int(input())
    number_list = deque(map(int, input().split()))
    count = 1
    while True:
        if number_list[0] - count <= 0:
            number_list.popleft()
            number_list.append(0)
            break
        else:
            number_list.append(number_list.popleft() - count)

        count = (count + 1) % 6
        if count == 0:
            count = 1

    print(f"#{tc}", *number_list)
