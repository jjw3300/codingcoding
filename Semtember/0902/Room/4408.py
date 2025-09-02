T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    room_num = []

    for _ in range(n):
        a, b = map(int, input().split())
        room_num.append((a, b))

    max_room = [0] * 201

    for start, goal in room_num:
        sta = (min(start, goal) + 1) // 2
        end = (max(start, goal) + 1) // 2
        for num in range(sta, end + 1):
            max_room[num] += 1

    answer = max(max_room)
    print(f"#{tc} {answer}")
