T = 10

for tc in range(1, T+1):
    n = int(input())
    word_list = [input() for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8 - n + 1):
            if word_list[i][j: j + n] == word_list[i][j: j + n][::-1]:
                count += 1

            column_list = []
            for a in range(j, j + n):
                column_list.append(word_list[a][i])
            if column_list == column_list[::-1]:
                count += 1

    print(f'#{tc} {count}')
