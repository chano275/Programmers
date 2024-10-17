from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

ans_time, ans = 0, 0

while 1:
    # print('#########################################')
    # for line in maps:print(line)
    ans_time += 1
    visited = [[False] * m for _ in range(n)]



    ### i, j 테두리 돌면서 각각의 bfs > 찍을 수 있는 곳 모두 -1로 지울떄마다 ㄱㄱㄱ?
    for i in  range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:  # 테두리
                if visited[i][j] == False and maps[i][j] in {0, -1}:

                    maps[i][j] = -1
                    visited[i][j] = True

                    queue = deque([(i, j)])
                    while queue:
                        cx, cy = queue.popleft()
                        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                            nx, ny = cx+dx, cy+dy
                            if maps[nx][ny] == 1: continue
                            if visited[nx][ny] == False:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                maps[nx][ny] = -1


    # print('#########################################')
    # for line in maps:print(line)

    maps_copy = [row[:] for row in maps]


    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:  # check : 4방향에 -1이 있으면 out
                flag = 0
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = i+dx, j+dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
                    if maps[nx][ny] == -1:
                        flag = 1
                        break

                if flag == 1:maps_copy[i][j] = 0
                else:maps_copy[i][j] = 1

            else:
                maps_copy[i][j] = maps[i][j]


    one_flag = 0
    for p in range(n):
        for q in range(m):
            if maps_copy[p][q] == 1:
                one_flag = 1
                break
        if one_flag == 1:break

    if one_flag == 1:
        maps = [row[:] for row in maps_copy]
        continue

    else:  # maps 돌면서 1인거 더하기
        chk = 0
        for p in range(n):
            for q in range(m):
                if maps[p][q] == 1:
                    chk += 1

        ans = chk
        break

print(ans_time)
print(ans)