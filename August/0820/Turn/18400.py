from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    number_list = deque(map(int, input().split()))

    for _ in range(m):
        number_list.append(number_list.popleft())

    print(f"#{tc} {number_list.popleft()}")
