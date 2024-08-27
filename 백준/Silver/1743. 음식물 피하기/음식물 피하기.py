from collections import deque


def bfs(_visited, cxy):
    temp = 0
    cx, cy = cxy
    queue = deque()
    queue.append((cx, cy))

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
            if _visited[nx][ny]:continue
            if maps[nx][ny] == 0:continue

            queue.append((nx, ny))
            _visited[nx][ny] = True
            temp += 1

    return temp


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
n,m,k = list(map(int, input().split()))
trash = [list(map(int, input().split())) for _ in range(k)]
maps = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]


for t in trash:
    maps[t[0] - 1][t[1] - 1] = 1

ans = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == False:
            ans = max(ans, bfs(visited, (i, j)))

print(ans)