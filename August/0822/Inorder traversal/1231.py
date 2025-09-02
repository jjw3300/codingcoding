def inorder(root_num):
    if root_num * 2 <= n:
        inorder(root_num * 2)
    answer.append(grape[root_num-1][1])
    if root_num * 2 + 1 <= n:
        inorder(root_num * 2 + 1)


T = 10
for tc in range(1, T + 1):
    n = int(input())
    grape = [list(input().split()) for _ in range(n)]
    answer = []

    inorder(1)
    print(f'#{tc}', ''.join(answer))
