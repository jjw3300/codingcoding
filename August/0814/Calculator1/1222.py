T = 10
for tc in range(1, T + 1):
    n = int(input())
    math_number = input()
    number = []
    stack = []
    for i in math_number:
        if i != '+':
            number.append(int(i))
        elif i == '+':
            if not stack:
                stack.append(i)
            elif stack:
                number += stack.pop()
                stack.append(i)
    for i in stack:
        number += i

    stack = []
    for i in number:
        if i != '+':
            stack.append(i)
        elif i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)

    print(f"#{tc} {stack[0]}")
