T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    pascal = [0, 1]

    print(f"#{tc}")
    for i in range(1, n + 1):
        for j in range(i):
            pascal[i-j] = pascal[i-j] + pascal[i-j-1]
            print(pascal[i-j], end=' ')
            pascal.append(0)
        print()
