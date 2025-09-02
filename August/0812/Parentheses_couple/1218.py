T = 10
for tc in range(1, T + 1):
    words_len = int(input())
    words = str(input())
    count = []

    answer = True
    for i in words:
        if i == '(':
            count.append('(')
        elif i == ')':
            if len(count) > 0:
                if count.pop() != '(':
                    answer = False
                    break
            else:
                answer = False
                break

        elif i == '[':
            count.append('[')
        elif i == ']':
            if len(count) > 0:
                if count.pop() != '[':
                    answer = False
                    break
            else:
                answer = False
                break

        elif i == '{':
            count.append('{')
        elif i == '}':
            if len(count) > 0:
                if count.pop() != '{':
                    answer = False
                    break
            else:
                answer = False
                break

    for i in words:
        if i == '<':
            count.append('<')
        elif i == '>':
            if len(count) > 0:
                if count.pop() != '<':
                    answer = False
                    break
            else:
                answer = False
                break

    if len(count) != 0:
        answer = False

    if answer:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")
