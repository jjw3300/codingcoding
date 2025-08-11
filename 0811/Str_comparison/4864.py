T = int(input())
for tc in range(1, T + 1):
    sub_word = input()
    main_word = input()
    count = 0
    i = 0

    if_in = False
    while i <= len(main_word) - len(sub_word):
        if main_word[i:i + len(sub_word)][-1] != sub_word[-1]:
            i += len(sub_word)
        elif main_word[i:i + len(sub_word)][-1] == sub_word[-1]:
            for j in range(1, len(sub_word) + 1):
                if main_word[i:i + len(sub_word)][-1 - j] == sub_word[-1 - j]:
                    if_in = True
                    continue
                else:
                    if_in = False
                    i += j
                    break
        else:
            i += 1

    if if_in:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
