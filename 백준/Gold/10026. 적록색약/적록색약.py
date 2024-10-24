from collections import deque


def bfs(v, start_point, mode):
    sx, sy = start_point

    if mode == 0:color = maps[sx][sy]
    else: color = maps_rg[sx][sy]

    queue = deque()
    queue.append((sx, sy))
    v[sx][sy] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
            if mode == 0:
                if v[nx][ny] == False and maps[nx][ny] == color:
                    v[nx][ny] = True
                    queue.append((nx, ny))

            else:
                if v[nx][ny] == False and maps_rg[nx][ny] == color:
                    v[nx][ny] = True
                    queue.append((nx, ny))


n = int(input())
maps = [list(map(str, input())) for _ in range(n)]
maps_rg = [m[:] for m in maps]

for i in range(n):
    for j in range(n):
        if maps_rg[i][j] == 'G':maps_rg[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
visited_rg = [[False] * n for _ in range(n)]

ans1, ans2 = 0,0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            # print(i, j)
            bfs(visited, (i, j), 0)  # 0은 기본, 1은 rg
            ans1 += 1

        if not visited_rg[i][j]:
            bfs(visited_rg, (i, j), 1)  # 0은 기본, 1은 rg
            ans2 += 1

print(f'{ans1} {ans2}')