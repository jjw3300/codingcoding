T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    answer = 0
    for x in range(-n, n+1):
        for y in range(-n, n+1):
            if x*x + y*y <= n*n:
                answer += 1
    print(f"#{tc} {answer}")
