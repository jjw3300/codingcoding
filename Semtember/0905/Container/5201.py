T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck_limit = list(map(int, input().split()))
    weight.sort(reverse=True)
    truck_limit.sort(reverse=True)
    answer = 0
    for i in truck_limit:
        for j in weight:
            if i >= j:
                answer += j
                weight.remove(j)
                break
    print(f"#{tc} {answer}")
