def bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


def boyer_moore_search(text, pattern):

    n = len(text)
    m = len(pattern)
    if m == 0:
        return True

    bad_char = bad_char_table(pattern)
    start = 0
    while start <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[start + j]:
            j -= 1

        if j < 0:
            return True
        else:
            mismatch_char = text[start + j]
            last_index = bad_char.get(mismatch_char, -1)
            shift = max(1, j - last_index)
            start += shift

    return False


T = int(input())
for tc in range(1, T + 1):
    sub_word = input()
    main_word = input()

    if boyer_moore_search(main_word, sub_word):
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
