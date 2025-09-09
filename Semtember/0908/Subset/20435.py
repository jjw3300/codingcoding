def subset(index, total, number, goal):
    if index == len(number):
        if total == goal:
            return 1
        else:
            return 0
    subset_in = subset(index + 1, total + number[index], number, goal)
    subset_not_in = subset(index + 1, total, number, goal)
    return subset_in + subset_not_in


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = subset(0, 0, numbers, k)
    print(f"#{tc} {answer}")
