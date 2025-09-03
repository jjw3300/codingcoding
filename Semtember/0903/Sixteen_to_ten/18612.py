T = int(input())
for tc in range(1, T + 1):
    temp_num = input().strip()

    bin_num = ''
    for c in temp_num:
        num = int(c, 16)
        b = bin(num)[2:]
        b = b.zfill(4)
        bin_num += b

    answer = []
    for i in range(0, len(bin_num), 7):
        temp = bin_num[i:i + 7]
        answer.append(int(temp, 2))

    print(f"#{tc}", *answer)