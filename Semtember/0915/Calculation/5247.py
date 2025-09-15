from collections import deque


def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = 1

    while queue:
        x, t = queue.popleft()
        if x == m:
            return t

        for nx in (x - 1, x + 1, x * 2, x - 10):
            if not (0 <= nx <= locate):
                continue
            if visited[nx]:
                continue
            visited[nx] = 1
            queue.append((nx, t + 1))


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    locate = 1000000
    visited = [0] * (locate + 1)
    print(f"#{tc} {bfs(n)}")
