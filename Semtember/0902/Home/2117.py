from collections import deque

T = 10
for tc in range(1, T + 1):
    n = int(input())
    operator = deque()
    number = [0 for i in range(n + 1)]
    for i in range(n):
        temp = list(map(str, input().split()))
        if len(temp) == 4:
            operator.append(temp)
        else:
            a, b = int(temp[0]), int(temp[1])
            number[a] = b

    while operator:
        node, opera, x, y = operator.pop()
        node = int(node)
        x = int(x)
        y = int(y)
        if opera == '+':
            number[node] = number[x] + number[y]
        elif opera == '-':
            number[node] = number[x] - number[y]
        elif opera == '*':
            number[node] = number[x] * number[y]
        elif opera == '/':
            number[node] = number[x] // number[y]

    print(f"#{tc} {number[1]}")
