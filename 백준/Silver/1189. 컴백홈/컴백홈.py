def dfs(_visited, cxy, depth):
    global ans

    cx, cy = cxy
    if (cx, cy) == end_point:
        if depth == k - 1:
            ans += 1
        return

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or ny < 0 or nx >= r or ny >= c:continue
        if maps[nx][ny] == 'T':continue
        if _visited[nx][ny]:continue

        _visited[nx][ny] = True
        dfs(_visited, (nx, ny), depth + 1)
        _visited[nx][ny] = False

    return


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
r,c,k = list(map(int, input().split()))
maps = [list(map(str, input())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

# for m in maps:    print(m)

ans = 0
start_point, end_point = (r-1,0), (0, c-1)

visited[start_point[0]][start_point[1]] = True
dfs(visited, start_point, 0)

print(ans)