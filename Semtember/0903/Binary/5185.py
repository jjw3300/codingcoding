T = int(input())
for tc in range(1, T + 1):
    n, temp_number = input().split()
    answer = bin(int(temp_number, 16))[2:].zfill(n * 4)
    print(f"#{tc} {answer}")
