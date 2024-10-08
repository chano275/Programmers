from collections import deque


def bfs(cxy, visit):
    queue = deque()
    queue.append(cxy)
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        visit[cx][cy] = True
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
            if visit[nx][ny] or maps[nx][ny] == '0':continue
            queue.append((nx, ny))
            visit[nx][ny] = True
            cnt += 1

    return cnt


n = int(input())
maps = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == '1':
            ans.append(bfs((i, j), visited))

print(len(ans))
ans = sorted(ans)
for a in ans: print(a)