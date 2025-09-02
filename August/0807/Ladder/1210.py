import sys

sys.stdin = open('input.txt')

T = 10

for i in range(1, T + 1):
    n = int(input())
    area = []
    for _ in range(100):  # 사다리 리스트 입력
        area.append(list(map(int, input().split())))

    goal_locate = []  # 목표 좌표 저장용 리스트
    for row_index, row in enumerate(area):  # 외부 리스트 인덱스, 내부 리스트
        for column_index, number in enumerate(row):  # 내부 리스트 인덱스, 내부 값
            if number == 2:  # 값이 2라면
                goal_locate.append(row_index)  # 외부 인덱스 좌표 저장
                goal_locate.append(column_index)  # 내부 인덱스 좌표 저장
    locate_row = goal_locate[0]  # 좌표 할당
    locate_column = goal_locate[1]  # 좌표 할당

    answer = 0  # 임시 값 할당
    while locate_row > 0:
        if locate_column > 0 and area[locate_row][locate_column - 1] == 1:
            while locate_column > 0 and area[locate_row][locate_column - 1] == 1:
                locate_column -= 1
            locate_row -= 1

        elif locate_column < 99 and area[locate_row][locate_column + 1] == 1:
            while locate_column < 99 and area[locate_row][locate_column + 1] == 1:
                locate_column += 1
            locate_row -= 1

        else:
            locate_row -= 1
        answer = locate_column

    print(f'#{i} {answer}')

