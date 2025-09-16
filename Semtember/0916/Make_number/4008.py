from collections import deque


def dfs(a, temp):
    global max_answer, min_answer, add, sub, mul, div
    if a == n:
        max_answer = max(max_answer, temp)
        min_answer = min(min_answer, temp)

    if add > 0:
        add -= 1
        dfs(a + 1, temp + number[a])
        add += 1

    if sub > 0:
        sub -= 1
        dfs(a + 1, temp - number[a])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(a + 1, temp * number[a])
        mul += 1

    if div > 0:
        div -= 1
        dfs(a + 1, int(temp / number[a]))
        div += 1


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    add, sub, mul, div = map(int, input().split())
    number = deque(map(int, input().split()))

    max_answer = -float('inf')
    min_answer = float('inf')

    dfs(1, number[0])
    print(f"#{tc} {int(max_answer) - int(min_answer)}")


