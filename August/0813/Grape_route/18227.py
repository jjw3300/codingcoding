import sys

sys.stdin = open('input.txt')


def dfs(graph, start_node):
    visited, need_visited = list(), list()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        if node == 99:
            return True
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph.get(node, []))

    return False


T = 10
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    join_list = list(map(int, input().split()))
    locate = dict()

    for i in range(0, len(join_list), 2):
        if join_list[i] not in locate:
            locate[join_list[i]] = [join_list[i+1]]
        elif join_list[i] in locate:
            locate[join_list[i]].append(join_list[i+1])

    if dfs(locate, 0):
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
