import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())

for i in range(1, T+1):
    num, length = map(str, input().split())
    num_length = int(length)
    str_list = list(input().split())
    num_list = []
    for j in str_list:
        if j == 'ZRO':
            num_list.append('0')
        elif j == 'ONE':
            num_list.append('1')
        elif j == 'TWO':
            num_list.append('2')
        elif j == 'THR':
            num_list.append('3')
        elif j == 'FOR':
            num_list.append('4')
        elif j == 'FIV':
            num_list.append('5')
        elif j == 'SIX':
            num_list.append('6')
        elif j == 'SVN':
            num_list.append('7')
        elif j == 'EGT':
            num_list.append('8')
        elif j == 'NIN':
            num_list.append('9')

    def max_list(a, b):
        for k in range(b - 1):
            min_idx = k
            for n in range(k + 1, b):
                if a[min_idx] > a[n]:
                    min_idx = n
            a[k], a[min_idx] = a[min_idx], a[k]
        return a

    num_list = max_list(num_list, len(num_list))
    answer_list = []

    for j in num_list:
        if j == '0':
            answer_list.append('ZRO')
        elif j == '1':
            answer_list.append('ONE')
        elif j == '2':
            answer_list.append('TWO')
        elif j == '3':
            answer_list.append('THR')
        elif j == '4':
            answer_list.append('FOR')
        elif j == '5':
            answer_list.append('FIV')
        elif j == '6':
            answer_list.append('SIX')
        elif j == '7':
            answer_list.append('SVN')
        elif j == '8':
            answer_list.append('EGT')
        elif j == '9':
            answer_list.append('NIN')

    print(f'#{i}')
    print(*answer_list)
