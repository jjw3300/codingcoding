T = int(input())
for tc in range(1, T + 1):
    a, b, c, d = list(map(int, input().split()))
    if a != 0 and b == 0 and c == 0 and d == 0:
        result = ("0" * (a + 1))
    elif a == 0 and b == 0 and c == 0 and d != 0:
        result = ("1" * (d + 1))
    elif b == c and b != 0:
        result = ("0" * (a + 1)) + ("10" * (b - 1)) + ("1" * (d + 1)) + "0"
    elif b - c == 1:
        result = ("0" * (a + 1)) + ("10" * c) + ("1" * (d + 1))
    elif c - b == 1:
        result = ("1" * (d + 1)) + ("01" * b) + ("0" * (a + 1))
    else:
        result = "impossible"

    print(f"#{tc} {result}")
