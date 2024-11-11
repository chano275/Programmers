from collections import deque


def bfs(start_point, v):
    queue = deque()
    queue.append(start_point)

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy

            if nx < 0 or ny < 0 or nx >= h or ny >= w:continue
            if v[nx][ny]:continue
            if maps[nx][ny] == '.':continue

            queue.append((nx, ny))
            v[nx][ny] = True

    return


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    maps = [list(map(str, input())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if (maps[i][j] == '#') and not visited[i][j]:
                visited[i][j] = True
                ans += 1
                bfs((i, j), visited)

    print(ans)