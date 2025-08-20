from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    pizza_list = deque(map(int, input().split()))
    count = 1
    stove = deque()
    pizza_count = 0
    pizza_index = deque()

    for i in range(n):
        stove.append(pizza_list.popleft())
        pizza_count += 1
        pizza_index.append(pizza_count)

    while True:

        if len(stove) == 1:
            break

        if stove[0] // 2 <= 0:
            stove.popleft()
            pizza_index.popleft()
            if pizza_list:
                stove.append(pizza_list.popleft())
                pizza_count += 1
                pizza_index.append(pizza_count)

        else:
            stove.append(stove.popleft() // 2)
            pizza_index.append(pizza_index.popleft())

    print(f"#{tc}", pizza_index[0])
