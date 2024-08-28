def dfs(_arr, _visited, cxy):
    cx, cy = cxy
    _visited[cx][cy] = True

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue

        if _arr[nx][ny] == 0 and _visited[nx][ny] == False:  # 0으로 들어왔는데, 0이면 그거의 주변 8칸도 visited 찍어야함
            dfs(_arr, _visited, (nx, ny))
        else: _visited[nx][ny] = True

    return


def dot_checker(arr):
    for a in arr:
        if False in a:
            return False
    return True


T = int(input())
dxy = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
for tc in range(1, T+1):
    n = int(input())  # 표 size
    maps = [list(map(str, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    ans = 0

    for i in range(n):
        for j in range(n):
            if maps[i][j] == '.':
                chk = 0
                for dx, dy in dxy:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                    if maps[nx][ny] == '*': chk += 1
                maps[i][j] = chk

            elif maps[i][j] == '*':                visited[i][j] = True

    # for m in maps:
    #     print(m)

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0 and not visited[i][j]:
                dfs(maps, visited, (i, j))
                ans += 1

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                ans += 1

    print(f'#{tc} {ans}')