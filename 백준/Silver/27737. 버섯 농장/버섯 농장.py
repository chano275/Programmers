from collections import deque


def bfs(start_point, v):
    ret = 0
    queue = deque()
    queue.append(start_point)

    while queue:
        cx, cy = queue.popleft()
        ret += 1

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
            if maps[nx][ny] == 1:continue
            if v[nx][ny]: continue

            v[nx][ny] = True
            queue.append((nx, ny))

    return ret


n, m, k = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

flag = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 0 and not visited[i][j]:
            flag = 1
            visited[i][j] = True
            temp = bfs((i, j), visited)
            # print(temp)
            while 1:
                if m == 0:break
                if temp <= 0:
                    temp = 0
                    break
                else:
                    temp -= k
                    m -= 1
if flag == 0:print('IMPOSSIBLE')
else:
    if m <= 0: print('IMPOSSIBLE')
    else:
        print('POSSIBLE')
        print(m)