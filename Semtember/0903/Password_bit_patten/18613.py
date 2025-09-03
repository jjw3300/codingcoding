pw_pattern = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
              '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}

T = int(input())
for tc in range(1, T + 1):
    answer = ""
    temp_number = input().strip()
    bin_number = bin(int(temp_number, 16))[2:].zfill(len(temp_number) * 4)

    i = 0
    for _ in range(len(bin_number)):
        if i > len(bin_number) - 6:
            break

        value = bin_number[i:i + 6]
        number = pw_pattern.get(value)
        if number is not None:
            answer += str(number)
            i += 6
        else:
            i += 1

    print(f"#{tc} {' '.join(answer)}")
