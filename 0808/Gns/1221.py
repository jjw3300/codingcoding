T = int(input())

alien_num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
             'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
arabic_num = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR',
              5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

for i in range(1, T+1):
    num, length = input().split()
    numbers = input().split()
    count = [0] * 10

    for j in numbers:
        count[alien_num[j]] += 1

    print(num)
    for j in range(10):
        print((arabic_num[j] + ' ') * count[j], end='')
