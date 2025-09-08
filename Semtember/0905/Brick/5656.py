from collections import deque
from copy import deepcopy

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = float('inf')


def bfs(row, col, board):
    queue = deque()
    if board[row][col] == 0:
        return
    queue.append((row, col, board[row][col]))
    board[row][col] = 0
    while queue:
        x, y, explosion = queue.popleft()
        for dx, dy in delta:
            for c in range(explosion):
                nx = x + dx * c
                ny = y + dy * c
                if 0 <= nx < m and 0 <= ny < n:
                    if board[nx][ny] != 0:
                        queue.append((nx, ny, board[nx][ny]))
                        board[nx][ny] = 0


def gravity(board):
    for j in range(n):
        stack = []
        for i in range(m - 1, -1, -1):
            if board[i][j] != 0:
                stack.append(board[i][j])
                board[i][j] = 0
        i = m-1
        for val in stack:
            board[i][j] = val
            i -= 1


def count_bricks(board):
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] != 0:
                count += 1
    return count


def find_start(k, board):
    global answer
    if k == marble:
        answer = min(answer, count_bricks(board))
        return
    for col in range(n):
        row = -1
        for r in range(m):
            if board[r][col] != 0:
                row = r
                break
        if row == -1:
            continue
        new_board = deepcopy(board)
        bfs(row, col, new_board)
        gravity(new_board)
        find_start(k+1, new_board)


T = int(input())
for tc in range(1, T+1):
    marble, n, m = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(m)]
    answer = float('inf')
    find_start(0, brick)
    if answer == float('inf'):
        answer = 0
    print(f"#{tc} {answer}")
