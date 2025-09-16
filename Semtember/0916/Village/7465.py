from collections import deque


def bfs(graph):
    visited = [False] * (n + 1)
    queue = deque()
    company = 0
    for num in range(1, n + 1):
        if not visited[num]:
            queue.append(num)
            company += 1
        while queue:
            value = queue.popleft()
            if not visited[value]:
                visited[value] = True
                for j in graph[value]:
                    queue.append(j)
    return company


T = int(input())
for tc in range(1, T + 1):

    n, m = map(int, input().split())

    graphs = [[] for _ in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        graphs[u].append(v)
        graphs[v].append(u)

    print(f"#{tc} {bfs(graphs)}")
