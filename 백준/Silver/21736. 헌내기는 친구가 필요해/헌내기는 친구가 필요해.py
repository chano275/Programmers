from collections import deque


def bfs(_visited, cxy):
    global ans

    cx, cy = cxy
    queue = deque()
    queue.append((cx, cy))
    _visited[cx][cy] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if _visited[nx][ny]:continue
            if maps[nx][ny] == 'X': continue

            queue.append((nx, ny))
            _visited[nx][ny] = True

            if maps[nx][ny] == 'P': ans += 1

    return


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
n, m = map(int, input().split())
maps = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            bfs(visited, (i, j))

if ans == 0: print('TT')
else:print(ans)

"""
I가 도연이 -> 출발좌표
X : 벽
0 : 빈 공간 
P : 사람
"""