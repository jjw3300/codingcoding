T = int(input())
for tc in range(1, T + 1):
    main_word, sub_word = input().split()
    count = 0
    i = 0

    while i <= len(main_word) - len(sub_word):
        if main_word[i:i + len(sub_word)] == sub_word:
            count += 1
            i += len(sub_word)
        else:
            i += 1

    answer = len(main_word) - count * (len(sub_word) - 1)
    print(f"#{tc} {answer}")
