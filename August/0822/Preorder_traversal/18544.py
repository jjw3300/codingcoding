def preorder(root_num):
    print(root_num, end=' ')
    for child in node[root_num]:
        preorder(child)


T = 1
for tc in range(1, T + 1):
    n = int(input())
    grape = list(map(int, input().split()))
    node = {}

    for i in range(1, n + 1):
        node[i] = []

    for i in range(n - 1):
        node[grape[2 * i]].append(grape[2 * i + 1])

    root = (set(node.keys()) - set(grape[1::2])).pop()

    preorder(root)
