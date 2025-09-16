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
                time = graph[nx][ny]
                if visited[nx][ny] > total + time:
                    visited[nx][ny] = total + time
                    heapq.heappush(queue, (total + time, nx, ny))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    print(f"#{tc} {dijkstra()}")
