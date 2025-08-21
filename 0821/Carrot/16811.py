T = int(input())

for tc in range(1, T + 1):
    carrot = int(input())
    carrot_carrot_carrot = list(map(int, input().split()))
    carrot_box_1 = []
    carrot_box_2 = []
    carrot_box_3 = []

    carrot_carrot_carrot.sort()

    for i in carrot_carrot_carrot:
        if carrot_carrot_carrot.count(i) > 1:
            if i in carrot_box_1 or i in carrot_box_2 or i in carrot_box_3:
                if i in carrot_box_1:
                    carrot_box_1.append(i)
                elif i in carrot_box_2:
                    carrot_box_2.append(i)
                elif i in carrot_box_3:
                    carrot_box_3.append(i)
            else:
                if len(carrot_box_1) - carrot_box_1.count(i) + carrot_carrot_carrot.count(i) < carrot / 3:
                    carrot_box_1.append(i)
                elif len(carrot_box_1) - carrot_box_1.count(i) + carrot_carrot_carrot.count(i) >= carrot // 3 \
                        > len(carrot_box_2) - carrot_box_2.count(i) + carrot_carrot_carrot.count(i):
                    carrot_box_2.append(i)
                elif len(carrot_box_1) - carrot_box_1.count(i) + carrot_carrot_carrot.count(i) >= carrot // 3 and \
                        len(carrot_box_2) - carrot_box_2.count(i) + carrot_carrot_carrot.count(i) >= carrot // 3:
                    carrot_box_3.append(i)

        else:
            if len(carrot_box_1) < carrot / 3:
                carrot_box_1.append(i)
            elif len(carrot_box_1) >= carrot // 3 > len(carrot_box_2):
                carrot_box_2.append(i)
            elif len(carrot_box_1) >= carrot // 3 and len(carrot_box_2) >= carrot // 3:
                carrot_box_3.append(i)

    carrot_answer = max(abs(len(carrot_box_1) - len(carrot_box_2)), abs(len(carrot_box_2) - len(carrot_box_3)),
                        abs(len(carrot_box_1) - len(carrot_box_3)))

    if carrot // 2 < len(carrot_box_1) or carrot // 2 < len(carrot_box_2) or carrot // 2 < len(carrot_box_3):
        carrot_answer = -1

    print(f'#{tc} {carrot_answer}')