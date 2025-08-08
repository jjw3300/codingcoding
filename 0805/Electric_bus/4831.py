T = int(input())
for i in range(1, T+1):
    max_move, goal_number, num_stations = map(int, input().split())
    station = [0]
    station = station + list(map(int, input().split()))
    station.append(goal_number)

    location = 0
    charge_count = 0

    for j in range(1, len(station)):

        if station[j] - station[j - 1] > max_move:
            charge_count = 0
            break

        if station[j] - location > max_move:
            location = station[j - 1]
            charge_count += 1

    print(f"#{i} {charge_count}")
