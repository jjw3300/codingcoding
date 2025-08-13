def join_paper(a):

    if a <= 1:
        return 1
    if a == 2:
        return 3
    else:
        return join_paper(a-1) + 2 * join_paper(a-2)


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} {join_paper(int(input()) // 10)}")
