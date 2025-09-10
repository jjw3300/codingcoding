def binary_search_changed(arr, target):
    left, right = 0, len(arr) - 1
    before_dire = None

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            if before_dire == 'L':
                return False
            before_dire = 'L'
            right = mid - 1
        else:
            if before_dire == 'R':
                return False
            before_dire = 'R'
            left = mid + 1

    return False


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    list_a = sorted(list(map(int, input().split())))
    list_b = list(map(int, input().split()))

    count = 0
    for tar in list_b:
        if binary_search_changed(list_a, tar):
            count += 1

    print(f"#{tc} {count}")
