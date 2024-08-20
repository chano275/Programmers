def dfs(_maps, cxy, _visited, _dxy, _dxy_idx):
    cx, cy = cxy

    if _dxy_idx == 4:
        if cx == start_elem_x and cy == start_elem_y:  # 탈출조건
            ans.append(len(_visited))
        return

    _visited = _visited[:]
    _visited.append(_maps[cx][cy])  # 방문
    # print(_visited)

    nx, ny = cx + _dxy[_dxy_idx][0], cy + _dxy[_dxy_idx][1]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:  return  # 범위 밖이면 나가
    if _maps[nx][ny] in _visited:
        if nx == start_elem_x and ny == start_elem_y:  # 도착 각 < 이거랑 위에 탈출조건이랑 뭐가다르지?
            ans.append(len(_visited))
            return
        else:
            return

    dfs(_maps, (nx, ny), _visited, _dxy, _dxy_idx + 1)  # 꺾어
    dfs(_maps, (nx, ny), _visited, _dxy, _dxy_idx)      # 꺾지말고 가

    return


dxy = [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # 우하 좌하 좌상 우상
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    ans = []

    # 시작점이 행이 0, n-1 / 열이 n-1이면 안됨
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == n-1: continue
            # 시작점 가능
            start_elem_x, start_elem_y = i, j
            visited = []
            dfs(maps, (i, j), visited, dxy, 0)

    if ans == []: ans.append(-1)
    print(f'#{tc} {max(ans)}')

    # break