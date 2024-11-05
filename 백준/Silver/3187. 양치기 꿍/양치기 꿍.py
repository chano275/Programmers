from collections import deque


def bfs(start_point, v):
    queue = deque()
    queue.append(start_point)

    sh, wo = 0,0

    while queue:
        cx, cy = queue.popleft()

        if maps[cx][cy] == 'v': wo += 1
        elif maps[cx][cy] == 'k': sh += 1

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if maps[nx][ny] == '#':continue
            if v[nx][ny]: continue

            v[nx][ny] = True
            queue.append((nx, ny))

    return sh, wo


n, m = map(int, input().split())

maps = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

sheep, wolf = 0,0
for i in range(n):
    for j in range(m):
        if (maps[i][j] in ['.', 'v', 'k']) and not visited[i][j]:
            visited[i][j] = True
            s, w = bfs((i, j), visited)
            if s == 0:
                wolf += w
            elif w == 0:
                sheep += s
            else:
                if s > w:
                    sheep += s
                else:
                    wolf += w

print(f'{sheep} {wolf}')