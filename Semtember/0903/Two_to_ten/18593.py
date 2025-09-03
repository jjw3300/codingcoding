T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    number = []
    for _ in range(n):
        number.extend(input().strip())
    answer = []
    temp = []
    count = 0
    for i in number:
        temp.append(i)
        if count == 6:
            count = 0
            answer.append(int(''.join(temp), 2))
            temp = []
        else:
            count += 1

    print(f"#{tc}", *answer)
