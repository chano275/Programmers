from collections import deque


def bfs(v, start_point):
    queue = deque()
    queue.append(start_point)

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = dx+cx, cy+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
            if v[nx][ny]:continue
            if rain_maps[nx][ny] == 1:continue

            queue.append((nx, ny))
            v[nx][ny] = True

    return


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

max_num = 0
min_num = float('inf')

for m in maps:
    max_num = max(max_num, max(m))
    min_num = min(min_num, min(m))

ans = 1

for height in range(min_num, max_num + 1):
    temp_ans = 0
    rain_maps = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] <= height:
                rain_maps[i][j] = 1  # 물로 가득 참

    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if rain_maps[i][j] == 0 and visited[i][j] == False:
                temp_ans += 1
                visited[i][j] = True
                bfs(visited, (i, j))

    ans = max(ans, temp_ans)

print(ans)