from collections import deque


def bfs(start, goal):
    queue = deque([[start, 0]])
    visited = [start]
    while True:
        if len(queue) == 0:
            break

        locate = queue.popleft()
        for node in graph[locate[0]]:
            if node == goal:
                return locate[1] + 1
            if node not in visited:
                queue.append([node, locate[1] + 1])
                visited.append(node)
    return 0


T = int(input())
for tc in range(1, T + 1):
    graph = {}
    v, e = map(int, input().split())
    for i in range(1, v + 1):
        graph[i] = []
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start_locate, goal_locate = map(int, input().split())
    print(f'#{tc} {bfs(start_locate, goal_locate)}')
