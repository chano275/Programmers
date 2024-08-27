from collections import deque


def bfs(_visited, cxy):
    cx, cy = cxy
    queue = deque()
    queue.append((cx, cy))
    _visited[cx][cy] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n:continue
            if _visited[nx][ny]:continue
            if maps[nx][ny] == 0:continue

            queue.append((nx, ny))
            _visited[nx][ny] = True

    return


dxy = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
m,n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

ans = 0
for i in range(m):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == False:
            bfs(visited, (i, j))
            ans += 1

print(ans)