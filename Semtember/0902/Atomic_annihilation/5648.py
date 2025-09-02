T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atomic = []
    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for _ in range(N):
        x, y, dire, energy = map(int, input().split())
        atomic.append([x * 2, y * 2, dire, energy])

    result = 0

    while atomic:
        positions = {}
        for i in range(len(atomic)):
            x, y, dire, energy = atomic[i]
            nx, ny = x + delta[dire][0], y + delta[dire][1]
            atomic[i][0], atomic[i][1] = nx, ny

            if (nx, ny) not in positions:
                positions[(nx, ny)] = []
            positions[(nx, ny)].append(i)

        remove_set = set()
        for pos, idx_list in positions.items():
            if len(idx_list) >= 2:

                result += sum(atomic[i][3] for i in idx_list)
                remove_set.update(idx_list)

        new_atomic = []
        for i in range(len(atomic)):
            if i not in remove_set:
                atom = atomic[i]
                if -4000 <= atom[0] <= 4000 and -4000 <= atom[1] <= 4000:
                    new_atomic.append(atom)

        atomic = new_atomic

    print(f"#{tc} {result}")
