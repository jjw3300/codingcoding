T = int(input())
for i in range(1, T + 1):
    n = int(input())

    a, b, c, d, e = 0, 0, 0, 0, 0

    while int(n / 2) == float(n / 2):
        n = n / 2
        a += 1

    while int(n / 3) == float(n / 3):
        n = n / 3
        b += 1

    while int(n / 5) == float(n / 5):
        n = n / 5
        c += 1

    while int(n / 7) == float(n / 7):
        n = n / 7
        d += 1

    while int(n / 11) == float(n / 11):
        n = n / 11
        e += 1

    print(f"#{i} {a} {b} {c} {d} {e}")
