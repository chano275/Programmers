from collections import deque


def bfs(start_point, ):
    visited = [[False] * w for _ in range(l)]
    queue = deque()
    queue.append(start_point)

    visited[start_point[0]][start_point[1]] = True
    ret = -1

    while 1:
        if not queue:return ret

        temp_queue = deque()

        ret += 1

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = cx+dx, cy+dy

                if nx < 0 or ny < 0 or nx >= l or ny >= w:continue
                if maps[nx][ny] == 'W':continue
                if visited[nx][ny]:continue

                visited[nx][ny] = True
                temp_queue.append((nx, ny))

        queue = temp_queue


l, w = map(int, input().split())
maps = [list(map(str, input())) for _ in range(l)]  # 모든 L에서 BFS 돌려서 NX 갈때마다 +1?

ans = 0

for i in range(l):
    for j in range(w):
        if maps[i][j] == 'L':  # 여기서 visited 찍고 들어가기는 좀? 한번 들어갈때마다 visited 갱신하는게 나아보이는데
            ans = max(ans, bfs((i, j)))

print(ans)