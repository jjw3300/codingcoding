from collections import deque


def bfs(start):
    distance = [-1] * n
    queue = deque([start])
    distance[start] = 0
    while queue:
        node = queue.popleft()
        for vortex in graph[node]:
            if distance[vortex] == -1:
                distance[vortex] = distance[node] + 1
                queue.append(vortex)
    return sum(distance)


T = int(input())
for tc in range(1, T + 1):
    temp_list = list(map(int, input().split()))
    n = temp_list[0]
    num_list = temp_list[1:]

    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if num_list[i * n + j] == 1:
                graph[i].append(j)

    min_dist = float('inf')
    for i in range(n):
        min_dist = min(min_dist, bfs(i))

    print(f"#{tc} {min_dist}")
