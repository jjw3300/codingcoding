def dfs(graph, v, visited):
    visited[v] = 1
    for vortex in graph[v]:
        if not visited[vortex]:
            dfs(graph, vortex, visited)


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    group = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    for i in range(0, m * 2, 2):
        a, b = group[i], group[i + 1]
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(n + 1)]
    group_count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            group_count += 1

    print(f"#{tc} {group_count}")
