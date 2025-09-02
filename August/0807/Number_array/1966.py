T = int(input())

for i in range(1, T+1):
    def max_list(a, b):
        for j in range(b - 1):
            min_idx = j
            for k in range(j + 1, b):
                if a[min_idx] > a[k]:
                    min_idx = k
            a[j], a[min_idx] = a[min_idx], a[j]
        return a
    n = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = max_list(num_list, n)

    print(f'#{i}', *sorted_list)
