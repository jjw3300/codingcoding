T = int(input())
for tc in range(1, T + 1):
    robot_order = list(map(str, input().split()))

    button = int(robot_order.pop(0))
    order = []
    for i in range(button):
        order.append([robot_order.pop(0), robot_order.pop(0)])

    b_locate = 1
    b_timing = 0
    b_click = []
    b_first = False

    o_locate = 1
    o_timing = 0
    o_click = []
    o_first = False

    for i in order:
        if i[0] == 'B':
            b_first = True
            while b_locate != int(i[1]):
                if b_locate < int(i[1]):
                    b_timing += 1
                    b_locate += 1

                elif b_locate > int(i[1]):
                    b_timing += 1
                    b_locate -= 1

            if o_first and b_timing < o_timing:
                b_timing = o_timing

            b_timing += 1
            b_click.append(b_timing)

            while b_timing in o_click:
                b_timing += 1
                b_click.pop()
                b_click.append(b_timing)

        if i[0] == 'O':
            o_first = True
            while o_locate != int(i[1]):
                if o_locate < int(i[1]):
                    o_timing += 1
                    o_locate += 1

                elif o_locate > int(i[1]):
                    o_timing += 1
                    o_locate -= 1

            if b_first and o_timing < b_timing:
                o_timing = b_timing

            o_timing += 1
            o_click.append(o_timing)

            while o_timing in b_click:
                o_timing += 1
                o_click.pop()
                o_click.append(o_timing)

    count = max(b_timing, o_timing)
    print(f"#{tc} {count}")
