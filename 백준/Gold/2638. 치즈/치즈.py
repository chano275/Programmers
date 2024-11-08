from collections import deque


def bfs(pass_list):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    maps[0][0] = -1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny]: continue
            if maps[nx][ny] in pass_list: continue

            visited[nx][ny] = True
            maps[nx][ny] = -1
            queue.append((nx, ny))


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 맨 처음 밖 -1로 만들기
bfs([1])  # -1 뻈음


ans = 0

while 1:
    # for _m in maps:print(_m)
    # print('##############################')
    # -1로 채워져 있는지 확인
    check_sum = 0
    for ma in maps:
        check_sum += sum(ma)
    if check_sum == -1 * (n*m):
        print(ans)
        break

    # 1 체크
    minus_list = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                minus_counter = 0
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

                    if maps[nx][ny] == -1:
                        minus_counter += 1

                if minus_counter >= 2:minus_list.append((i, j))

    for minus in minus_list:
        maps[minus[0]][minus[1]] = -1

    # -1 or 0에서 bfs 때려서 0 만나면 거기부터 -1로 ?
    bfs([1])

    ans += 1


