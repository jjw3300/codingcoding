T = int(input())
for tc in range(1, T + 1):
    n = float(input())
    answer = ""
    count = 0

    while n > 0:
        if count >= 12:
            answer = "overflow"
            break
        n *= 2
        if n >= 1:
            answer += "1"
            n -= 1
        else:
            answer += "0"
        count += 1

    print(f"#{tc} {answer}")
