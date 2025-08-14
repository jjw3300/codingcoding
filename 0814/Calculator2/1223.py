T = 10
for tc in range(1, T + 1):
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

    n = int(input())
    math_number = input().strip()
    number = ''
    stack = []

    for i in math_number:
        if i not in '(+-*/)':
            number += i
        elif i == ')':
            while stack[-1] != '(':
                number += stack.pop()
            stack.pop()
        else:
            if not stack or isp[stack[-1]] < icp[i]:
                stack.append(i)
            else:
                while stack and isp[stack[-1]] >= icp[i]:
                    number += stack.pop()
                stack.append(i)
    while stack:
        number += stack.pop()

    for i in number:
        if i not in '+*':
            stack.append(i)
        elif i == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        elif i == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a * b)

    print(f"#{tc} {stack[0]}")
