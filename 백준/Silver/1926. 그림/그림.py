from collections import deque


def bfs(v, start):
    queue = deque()
    queue.append(start)

    v[start[0]][start[1]] = True

    ret = 0

    while queue:
        cx, cy = queue.popleft()
        # print((cx, cy))

        ret += 1  # 넓이 
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
            if maps[nx][ny] == 0:continue
            if v[nx][ny] == True:continue

            queue.append((nx, ny))
            v[nx][ny] = True

    return ret


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans_cnt, ans_val = 0, 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == False:
            ans_val = max(ans_val, bfs(visited, (i, j)))
            ans_cnt += 1

#            print((i, j), ans_val)

if ans_cnt == 0: 
    print(ans_cnt)
    print(0)

else:
    print(ans_cnt)
    print(ans_val)