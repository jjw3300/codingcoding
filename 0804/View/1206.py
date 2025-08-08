import sys

sys.stdin = open('sample_input.txt')

T = 10

for i in range(T):
    n = int(input())
    view_rights = 0
    building = list(map(int, input().split()))

    def min_num(args):
        min_number = args[0]
        for i in args:
            if i < min_number:
                min_number = i
        return min_number

    for j in range(2, n - 1):
        if building[j] > building[j-2] and building[j] > building[j-1]\
                and building[j] > building[j+1] and building[j] > building[j+2]:
            view_rights += min_num([building[j] - building[j-2], building[j] - building[j-1],
                               building[j] - building[j+1], building[j] - building[j+2]])

    print(f'#{i+1} {view_rights}')
