def inorder_traverse(node):
    global index

    if node > n:
        return

    inorder_traverse(node * 2)
    tree[node] = index
    index += 1
    inorder_traverse(node * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    tree = [0] * (n + 1)
    index = 1

    inorder_traverse(1)

    root = tree[1]
    n_2 = tree[n // 2]
    print(f'#{tc} {root} {n_2}')
