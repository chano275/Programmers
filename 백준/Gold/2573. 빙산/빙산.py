from collections import deque


def bfs(tv, start_point):
    queue = deque()
    queue.append(start_point)

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = dx + cx, dy + cy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
            if tv[nx][ny]:continue

            tv[nx][ny] = True
            queue.append((nx, ny))


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]  # n 행
ans = 0
while 1:
    ans += 1
    temp_maps = [[0] * m for _ in range(n)]
    temp_visited = [[True] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0:
                cx, cy = i, j
                temp = 0
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = dx+cx, dy+cy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
                    if maps[nx][ny] == 0:temp += 1

                if temp == 0:
                    temp_maps[i][j] = maps[cx][cy]
                    temp_visited[i][j] = False  # bfs 해야 하니까~
                else:
                    if maps[cx][cy] - temp <= 0:temp_maps[i][j] = 0
                    else:
                        temp_maps[i][j] = maps[cx][cy] - temp
                        temp_visited[i][j] = False  # bfs 해야 하니까~
            # else: 애초에 값이 0이니까 할 필요 없음

    # for t in temp_maps:print(t)

    # 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력
    temp_sum = 0
    for i in range(n):temp_sum += sum(temp_maps[i])
    if temp_sum == 0:
        print(0)
        break

    # temp_maps 통해서 bfs 돌려 덩어리 개수 확인 : 2 이상ㅇ
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and temp_visited[i][j] == False:
                bfs(temp_visited, (i, j))
                cnt += 1

    if cnt >= 2:
        print(ans)
        break

    maps = [ elem[:] for elem in temp_maps ]
    