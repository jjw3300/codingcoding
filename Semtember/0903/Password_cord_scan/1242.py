def analyze_password(password):
    for row in reversed(password):
        target = None
        for a in row:
            if a != 0:
                target = a
                break
        if target is None:
            pass
        else:
            if 'target' in row:
                idx = row.rfind('target')
                code = row[idx-55:idx+1]
                return code
    return None


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    password = [input().strip() for _ in range(n)]
    pattern = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
               '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    code = analyze_password(password)

    number = []
    for i in range(0, 56, 7):
        temp = code[i:i+7]
        number.append(pattern[temp])

    odd_sum = sum(number[0::2])
    even_sum = sum(number[1::2])
    if (odd_sum * 3 + even_sum) % 10 == 0:
        print(f"#{tc} {sum(number)}")
    else:
        print(f"#{tc} {0}")
