T = int(input())
for tc in range(1, T + 1):
    math_number = list(map(str, input().split()))
    stack = []

    for i in math_number:
        if i not in '+-*/.':
            stack.append(int(i))
        elif i in '+-*/':
            if len(stack) > 1:
                if i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif i == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b / a)
            else:
                print(f"#{tc} error")
                break

        elif i == '.':
            if len(stack) != 1:
                print(f"#{tc} error")
                break
            else:
                print(f"#{tc} {int(stack[-1])}")
                break
