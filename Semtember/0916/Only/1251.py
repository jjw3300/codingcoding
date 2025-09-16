def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        return True
    return False


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    e = float(input())

    island = list(zip(x_list, y_list))

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = island[i][0] - island[j][0]
            dy = island[i][1] - island[j][1]
            dist = dx * dx + dy * dy
            edges.append((dist, i, j))

    parent = [i for i in range(n)]
    edges.sort()
    temp_cost = 0
    for dist, u, v in edges:
        if union(u, v):
            temp_cost += dist

    total_cost = round(temp_cost * e)

    print(f"#{tc} {total_cost}")

