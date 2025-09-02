def dfs(graph, start_node):
    visited, need_visited = list(), list()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    join_list = [list(map(int, input().split())) for _ in range(e)]
    start, goal = map(int, input().split())

    locate = dict()
    for i, j in join_list:
        if i not in locate:
            locate[i] = [j]
        elif i in locate:
            locate[i].append(j)

    route = dfs(locate, start)
    if goal in route:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
