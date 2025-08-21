from collections import deque


def bfs(start):
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        number = queue.popleft()
        if number not in visited:
            visited.append(number)

        for route in node[number]:
            if route not in visited:
                queue.append(route)

    return visited


T = 1
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    join_list = list(map(int, input().split()))
    node = {}

    for i in range(1, 1+n):
        node[i] = []

    for i in range(m):
        node[join_list[2*i]].append(join_list[2*i+1])

    result = bfs(1)
    print(f"#{1}", *list(result[i] for i in range(n)))
