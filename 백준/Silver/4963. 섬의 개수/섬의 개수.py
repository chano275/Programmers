from collections import deque


def bfs(start_point, v):
    queue = deque()
    queue.append(start_point)

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
            nx, ny = cx+dx, cy+dy

            if nx < 0 or nx >= h or ny < 0 or ny >= w:continue
            if maps[nx][ny] == 0:continue
            if v[nx][ny]:continue

            v[nx][ny] = True
            queue.append((nx, ny))

    return 0


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    ans = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                bfs((i, j), visited)
                ans += 1

    print(ans)