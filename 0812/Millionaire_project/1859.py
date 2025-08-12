T = int(input())

for tc in range(1, T+1):
    days = int(input())
    sale_price = list(map(int, input().split()))

    buy_list = []
    sell_price = sale_price[-1]
    my_money = 0

    for i in range(days - 2, - 1, -1):

        if sale_price[i] <= sale_price[i + 1] and sell_price <= sale_price[i + 1]:
            buy_list.append(sale_price[i])
            sell_price = sale_price[i + 1]

        elif sale_price[i] <= sell_price:
            buy_list.append(sale_price[i])

        elif sell_price < sale_price[i]:
            for _ in range(len(buy_list)):
                my_money += sell_price - buy_list.pop()
            sell_price = 0

    for _ in range(len(buy_list)):
        my_money += sell_price - buy_list.pop()

    print(f'#{tc} {my_money}')
