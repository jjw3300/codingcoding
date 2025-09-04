def dfs(count):
    global numbers, max_money, unique_number

    temp = int(''.join(numbers))
    count_temp = (count, temp)
    if count_temp in unique_number:
        return
    unique_number.add(count_temp)

    if count == int(change):
        max_money = max(max_money, temp)
        return

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                continue

            numbers[i], numbers[j] = numbers[j], numbers[i]
            dfs(count + 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())

for tc in range(1, T + 1):
    number, change = input().split()
    numbers = list(number)
    max_money = 0
    unique_number = set()

    dfs(0)
    print(f"#{tc} {max_money}")
