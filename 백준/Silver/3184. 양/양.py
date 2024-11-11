from collections import deque


def bfs(start_point, v):
    queue = deque()
    queue.append(start_point)

    count_v, count_o = 0,0

    while queue:
        cx, cy = queue.popleft()

        if maps[cx][cy] == 'v':count_v += 1
        elif maps[cx][cy] == 'o':count_o += 1

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy

            if nx < 0 or ny < 0 or nx >= r or ny >= c:continue
            if v[nx][ny]:continue
            if maps[nx][ny] == '#':continue

            queue.append((nx, ny))
            v[nx][ny] = True

    if count_v >= count_o:return count_v, 0
    else:                 return 0, count_o


r, c = map(int, input().split())
maps = [list(map(str, input())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]


av, ao = 0,0
for i in range(r):
    for j in range(c):
        if (maps[i][j] == 'v' or maps[i][j] == 'o') and not visited[i][j]:  # v - 늑대 / o - 양
            visited[i][j] = True
            temp_v, temp_o = bfs((i, j), visited)
            av += temp_v
            ao += temp_o

print(ao, av)