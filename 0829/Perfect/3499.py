from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cards = list(map(str, input().split()))

    even = deque(cards[:(n+1)//2])
    odd = deque(cards[(n+1)//2:])

    answer = []
    for i in range(n//2 + 1):
        if even:
            answer.append(even.popleft())
        if odd:
            answer.append(odd.popleft())

    print(f"#{tc}", *answer)
