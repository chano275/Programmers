from collections import deque


dxy = [(2, 1), (2,-1), (-2,1), (-2,-1), (1, 2), (1,-2), (-1,2), (-1,-2)]
tc = int(input())
for _ in range(tc):
    l = int(input())
    x, y = map(int, input().split())
    ax, ay = map(int, input().split())

    maps_v = [[False] * l for _ in range(l)]
    maps_v[x][y] = True

    queue = deque()
    queue.append((x, y))

    depth = 0
    flag = 0

    if x == ax and y == ay:print(0)
    else:
        while 1:
            # for m in maps_v:print(m)
            temp_queue = deque()
            depth += 1

            while queue:
                cx, cy = queue.popleft()
                for dx, dy in dxy:
                    nx, ny = cx+dx, cy+dy
                    if nx < 0 or ny < 0 or nx >= l or ny >= l:continue
                    if maps_v[nx][ny]:continue

                    if nx == ax and ny == ay:
                        flag = 1
                        break

                    maps_v[nx][ny] = True
                    temp_queue.append((nx, ny))

                if flag == 1:break
            if flag == 1:break

            queue = temp_queue
            if not queue:break
        print(depth)