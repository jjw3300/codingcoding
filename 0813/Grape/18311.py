def dfs(graph, start_node):
    visited, need_visited = list(), list()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited


T = 1
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    join_list = list(map(int, input().split()))
    locate = dict()
    for i in range(len(join_list)-1, -1, -2):
        if join_list[i] not in locate and join_list[i-1] not in locate:
            locate[join_list[i]] = [join_list[i-1]]
            locate[join_list[i-1]] = [join_list[i]]
        elif join_list[i] in locate and join_list[i-1] not in locate:
            locate[join_list[i]].append(join_list[i-1])
            locate[join_list[i-1]] = [join_list[i]]
        elif join_list[i] not in locate and join_list[i-1] in locate:
            locate[join_list[i]] = [join_list[i-1]]
            locate[join_list[i-1]].append(join_list[i])
        elif join_list[i] in locate and join_list[i-1] in locate:
            locate[join_list[i]].append(join_list[i-1])
            locate[join_list[i-1]].append(join_list[i])

    answer = dfs(locate, 1)
    new_answer = []
    for i in answer:
        new_answer.append(str(i))

    print(f"#{tc}", "-".join(new_answer))
