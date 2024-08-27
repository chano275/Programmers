from collections import deque


def bfs(_visited, cxy):
    queue = deque()
    cx, cy = cxy
    queue.append((cx, cy))

    _visited[cx][cy] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
            if _visited[nx][ny]:continue
            if maps[nx][ny] == 0: continue

            _visited[nx][ny] = True
            queue.append((nx, ny))

    return





dxy = [(1,0), (0,1), (-1,0), (0,-1)]
T = int(input())
for _ in range(T):
    m, n, k = list(map(int, input().split()))

    ones = [list(map(int, input().split())) for _ in range(k)]
    maps = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for one in ones:
        maps[one[1]][one[0]] = 1

    ans = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j] == False:  # 방문 안했고 땅 발견:
                ans += 1
                bfs(visited, (i, j))

    print(ans)