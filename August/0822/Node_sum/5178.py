T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    node = [[] for _ in range(n + 1)]

    for i in range(m):
        parent, child = map(int, input().split())
        node[parent].append(child)

    for i in range(n, 1, -1):
        parent = i // 2
        node[parent] += node[i]

    print(f"#{tc} {sum(node[l])}")
