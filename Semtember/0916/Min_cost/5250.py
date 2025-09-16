import heapq


def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    visited = [[float('inf') for _ in range(n)] for _ in range(n)]
    visited[0][0] = 0

    while queue:
        total, x, y = heapq.heappop(queue)

        if x == n - 1 and y == n - 1:
            return total

        for dx, dy in delta:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                cost = 1 + max(0, graph[nx][ny] - graph[x][y])
                if visited[nx][ny] > total + cost:
                    visited[nx][ny] = total + cost
                    heapq.heappush(queue, (total + cost, nx, ny))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    print(f"#{tc} {dijkstra()}")
