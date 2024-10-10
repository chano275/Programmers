from collections import deque


tc = int(input())

for _ in range(tc):
    n = int(input())
    home_x, home_y = map(int, input().split())
    conv = [list(map(int, input().split())) for _ in range(n)]
    pent_x, pent_y = map(int, input().split())

    visited = set()
    flag = 0

#     if abs(pent_x - home_x) + abs(pent_y - home_y) <= 1000: print('happy')

#     else:

    queue = deque()
    queue.append((home_x, home_y))

    while queue:
        cx, cy = queue.popleft()
        # print(queue)
        # print(cx, cy)
        if abs(cx - pent_x) + abs(cy - pent_y) <= 1000:
            print('happy')
            flag = 1
            break

        for dx, dy in conv:
            if (dx, dy) in visited:continue


            if abs(dx - cx) + abs(dy - cy) <= 1000:  # 그냥 갈수있는데 다찍어
                queue.append((dx, dy))
                visited.add((dx, dy))

#        if flag == 1: break

    if flag == 1:continue
    else:print('sad')
