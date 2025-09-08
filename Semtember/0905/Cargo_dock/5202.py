T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    tasks = []
    for _ in range(n):
        start, end = map(int, input().split())
        tasks.append((end, start))

    tasks.sort()
    count = 0
    before_end = 0

    for end_time, start_time in tasks:
        if start_time >= before_end:
            count += 1
            before_end = end_time

    print(f"#{tc} {count}")
