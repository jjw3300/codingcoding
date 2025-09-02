T = int(input())
for i in range(1, T + 1):
    word_list = []
    for _ in range(5):
        word_list.append(list(map(str, input())))

    answer = []
    for a in range(15):
        for b in range(5):
            if len(word_list[b]) > a:
                answer.append(word_list[b][a])

    print(f"#{i}", ''.join(answer))
