from collections import deque

T = int(input())
for tc in range(1, T + 1):
    cards = deque(map(int, input().split()))
    player_1 = [0 for _ in range(10)]
    player_2 = [0 for _ in range(10)]
    answer = 0

    for _ in range(6):
        player_1[cards.popleft()] += 1
        player_2[cards.popleft()] += 1

        for i in range(2, 10):
            if player_1[i] != 0 and player_1[i-1] != 0 and player_1[i-2] != 0:
                answer = 1
                break
        for i in player_1:
            if i >= 3:
                answer = 1
                break
        if answer:
            break

        for i in range(2, 10):
            if player_2[i] != 0 and player_2[i - 1] != 0 and player_2[i - 2] != 0:
                answer = 2
                break
        for i in player_2:
            if i >= 3:
                answer = 2
                break
        if answer:
            break

    print(f"#{tc} {answer}")
