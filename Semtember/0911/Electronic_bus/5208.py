def backtracking(locate, count):
    global min_change

    if locate >= start - 1:
        min_change = min(min_change, count - 1)
        return

    if count >= min_change and start - 1 > locate:
        return

    for i in range(locate + 1, locate + bus_stop[locate] + 1):
        backtracking(i, count + 1)


T = int(input())
for tc in range(1, T + 1):
    bus_road = list(map(int, input().split()))
    start = bus_road[0]
    bus_stop = bus_road[1:]
    bus_stop.append(0)
    min_change = float('inf')

    backtracking(0, 0)
    print(f"#{tc} {min_change}")
