T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    word_list = [input() for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n - m + 1):
            if word_list[i][j: j + n] == word_list[i][j: j + n][::-1]:
                answer = word_list[i][j: j + n]

            column_list = []
            for a in range(j, j + m):
                column_list.append(word_list[a][i])
            if column_list == column_list[::-1]:
                answer = ''.join(column_list)

    print(f'#{tc}', answer)
