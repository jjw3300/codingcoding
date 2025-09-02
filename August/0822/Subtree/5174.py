from collections import deque


def bfs(graphs, start):
    visited = [False] * len(graphs)
    queue = deque([start])
    count = 0

    while queue:
        value = queue.popleft()
        if not visited[value]:
            visited[value] = True
            count += 1
            for j in graphs[value]:
                if not visited[j]:
                    queue.append(j)
    return count


T = int(input())
for tc in range(1, T + 1):
    e, n = map(int, input().split())
    grape = list(map(int, input().split()))

    node = [[] for _ in range(max(grape) + 1)]

    for i in range(e):
        parent, child = grape[2 * i], grape[2 * i + 1]
        node[parent].append(child)

    print(f"#{tc} {bfs(node, n)}")
