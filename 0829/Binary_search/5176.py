def inorder_traverse(node):
    global index

    left = node * 2
    right = node * 2 + 1

    if node > n:
        return
    inorder_traverse(left)

    tree[node] = index
    index += 1

    if node > n:
        return
    inorder_traverse(right)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    tree = [0 for i in range(n + 1)]
    index = 1
    inorder_traverse(1)

    root = tree[1]
    n_2 = tree[n // 2]
    print(f'#{tc} {root} {n_2}')
