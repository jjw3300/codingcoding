import heapq

T = int(input())
for tc in range(1, T + 1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    visited = [0] * (n + 1)
    queue = [(0, 0)]
    total_dist = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if visited[node] == 1:
            continue
        elif visited[node] == 0:
            visited[node] = 1
            total_dist += dist

        for i in graph[node]:
            if visited[i[0]] == 0:
                heapq.heappush(queue, (i[1], i[0]))

    print(f"#{tc} {total_dist}")
