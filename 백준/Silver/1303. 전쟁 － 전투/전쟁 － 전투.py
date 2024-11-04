from collections import deque


def bfs(start_point, v, color):
    queue = deque()
    queue.append(start_point)

    depth = 0

    while queue:
        cx, cy = queue.popleft()
        depth += 1

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
            if v[nx][ny]:continue
            if maps[nx][ny] != color: continue  # 다른색이면 ㄴㄴ

            v[nx][ny] = True
            queue.append((nx, ny))

    return depth


n, m = map(int, input().split())  # 가로 / 세로
maps = [list(map(str, input())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

ans1, ans2 = 0, 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True

            if maps[i][j] == 'W':
                ans1 += bfs((i, j), visited, maps[i][j]) ** 2

            else:
                ans2 += bfs((i, j), visited, maps[i][j]) ** 2


print(f'{ans1} {ans2}')