def dfs(cxy, r_idx, visited):
    global ans

    #print(visited)

    if r_idx == len(dxy):
        if cxy == start_point:            ans = max(ans, len(visited))
        return

    cx, cy = cxy
    dx, dy = dxy[r_idx]

    nx, ny = cx+dx, cy+dy
    if nx < 0 or ny < 0 or nx >= n or ny >= n:return
    if maps[nx][ny] in visited:
        if (nx, ny) == start_point: ans = max(ans, len(visited))
        return

    dfs((nx, ny), r_idx + 1, visited + [maps[nx][ny]])
    dfs((nx, ny), r_idx, visited + [maps[nx][ny]])

    return


dxy = [(-1,1), (1,1), (1,-1), (-1,-1)]
T = int(input())
for tc in range(1, T+1):
    n = int(input())

    maps = [list(map(int, input().split())) for _ in range(n)]

    ans = -1
    for i in range(n):
        for j in range(n):
            if i == 0 or j == n-1 or i == n-1: continue
            start_point = (i, j)
            dfs(start_point, 0, [maps[i][j]])

    print(f'#{tc} {ans}')