T = int(input())

for tc in range(1, T+1):
    case = input()
    laser_iron = case.replace('()', 'l')

    count_stick = 0
    current_stick = 0
    for i in laser_iron:
        if i == 'l':
            count_stick += current_stick
        elif i == '(':
            current_stick += 1
        elif i == ')':
            count_stick += 1
            current_stick -= 1

    print(f'#{tc} {count_stick}')
