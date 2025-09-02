T = int(input())

for i in range(1, T+1):
    word = input()
    reverse_word = word[::-1]
    answer_word = []
    for j in reverse_word:
        if j == 'b':
            answer_word.append('d')
        elif j == 'd':
            answer_word.append('b')
        elif j == 'p':
            answer_word.append('q')
        elif j == 'q':
            answer_word.append('p')

    print(f'#{i}', ''.join(answer_word))
