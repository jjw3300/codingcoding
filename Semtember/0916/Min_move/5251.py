import heapq

T = int(input())
for tc in range(1, T + 1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    distance = [float('inf')] * (n + 1)
    distance[0] = 0
    queue = [(0, 0)]

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue, (dist + i[1], i[0]))

    print(f"#{tc} {distance[n]}")
