from collections import deque


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    maps = [list(map(str, input())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    ans = 0

    queue = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny] != -1: continue
            # if maps[nx][ny] == 'W':continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[cx][cy] + 1
            ans += visited[nx][ny]

    # for asc in visited:print(asc)

    print(f'#{tc} {ans}')