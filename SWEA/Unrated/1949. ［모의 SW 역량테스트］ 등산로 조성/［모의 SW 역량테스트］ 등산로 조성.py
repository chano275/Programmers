def dfs(cxy, _maps, _visited, depth, _k_flag):
    cx, cy = cxy

    for dx, dy in dxy:
        nx, ny = cx+dx, cy+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:  continue  # 네모 밖으로 나가는거 말고
        if _visited[nx][ny]:  continue  # 방문했었던 곳은 가지말고

        if _maps[nx][ny] >= _maps[cx][cy]:
            if _k_flag == 0:  # flag 안썼어
                if _maps[nx][ny] - k <= _maps[cx][cy] - 1:  # 사용 가능 ?  /  _k_flag = 1 << 그냥 dfs 보낼때 1로 바꾸기
                    _visited = [p[:] for p in _visited]
                    _maps = [p[:] for p in _maps]

                    temp = _maps[nx][ny]

                    _maps[nx][ny] = _maps[cx][cy] - 1

                    _visited[cx][cy] = True
                    dfs((nx, ny), _maps, _visited, depth + 1, 1)
                    _visited[cx][cy] = False

                    _maps[nx][ny] = temp


                else:  continue

            else: continue

        else:
            # 갈곳 있고 정상? visited 찍고 가
            _visited = [p[:] for p in _visited]
            _maps = [p[:] for p in _maps]

            _visited[cx][cy] = True
            dfs((nx, ny), _maps, _visited, depth + 1, _k_flag)
            _visited[cx][cy] = False

    # 4방향 다 갈곳 없어? finished에 붙이고 나가
    finished.append(depth)
    return




dxy = [(1,0), (0,1), (-1,0), (0,-1)]
T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]

    max_elem = 0
    for m in maps:
        max_elem = max(max_elem, max(m))

    ans = 0
    finished = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == max_elem:
                k_flag = 0
                visited[i][j] = True
                dfs((i, j), maps, visited, 1, k_flag)
                visited[i][j] = False

    print(f'#{tc} {max(finished)}')