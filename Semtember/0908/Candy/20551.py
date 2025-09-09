T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    count = 0
    while True:
        if a <= 0 or b <= 0 or c <= 0:
            count = -1
            break
        if a < b < c:
            break
        elif b >= c:
            b -= 1
            count += 1
        elif a >= b:
            a -= 1
            count += 1

    print(f"#{tc} {count}")
