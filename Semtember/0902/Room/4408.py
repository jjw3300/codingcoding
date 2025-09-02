import heapq

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    heap = []
    for num in numbers:
        heapq.heappush(heap, num)

    temp = len(heap) - 1
    answer = 0
    while temp != 0:
        temp = (temp - 1) // 2
        answer += heap[temp]

    print(f"#{tc} {answer}")
