T = 10

for tc in range(1, T+1):
    words_len, words = map(str, input().split())
    words_len = int(words_len)
    words = list(words)
    count = 1

    while count != 0:
        count = 0
        for i in range(len(words) - 1):
            if words[i] == words[i+1]:
                words.pop(i)
                words.pop(i)
                count += 1
                break

    print(f'#{tc}', ''.join(words))
