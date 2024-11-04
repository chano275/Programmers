from collections import deque


def bfs(start_point, v):
    queue = deque()
    queue.append(start_point)

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n:continue
            if v[nx][ny]:continue
            if maps[nx][ny] == '1': continue

            v[nx][ny] = True
            queue.append((nx, ny))

    return


m, n = map(int, input().split())  # 행 열
maps = [list(map(str, input())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]


for i in range(n):  # 여기의 모든 0, i 에서 bfs 출발
    if maps[0][i] == '0' and not visited[0][i]:  #
        visited[0][i] = True
        bfs((0, i), visited)

flag = 0
for i in range(n):
    if visited[m-1][i]:
        flag = 1
        break

if flag == 0: print('NO')
else:print('YES')
