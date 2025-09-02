T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lines = []

    for _ in range(n):
        lines.append(list(map(int, input().split())))

    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            ai, bi = lines[i]
            aj, bj = lines[j]
            if (ai - aj) * (bi - bj) < 0:
                answer += 1

    print(f"#{tc} {answer}")
