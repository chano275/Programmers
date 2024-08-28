def dfs(_visited, _length, cxy):
    global ans
    cx, cy = cxy

    for dx, dy in dxy:
        nx, ny = dx + cx, dy + cy
        if nx < 0 or ny < 0 or nx >= r or ny >= c:continue
#        if _visited_list[nx][ny] == 1:continue
        if alpha[nx][ny] in _visited:continue

#        _visited_list[nx][ny] = 1
        _visited.add(alpha[nx][ny])
        dfs(_visited, _length + 1, (nx, ny))
        _visited.discard(alpha[nx][ny])
#        _visited_list[nx][ny] = 0

    # 갈곳이 없으면 나오겠지?

#    print(_visited)
    ans = max(ans, _length)
    return


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
r,c = map(int, input().split())
alpha = [list(map(str, input())) for _ in range(r)]

# 0,0 시작, 최대 칸수

ans = 0

#visited_list = [[0] * c for _ in range(r)]
#visited_list[0][0] = 1

visited = set()
visited.add(alpha[0][0])
dfs(visited, 1, (0,0))

print(ans)


