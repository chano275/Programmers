def dfs(cxy_idx, visited_list, core, l_len):

    #print(cxy_idx)

    if cxy_idx == len(cxy):  # 다 찍진 않았어도 끝까지 도달?
        result.append((core, l_len))
        return

    cx, cy = cxy[cxy_idx]

    if cx == 0 or cy == 0 or cx == n-1 or cy == n-1:  # 전기 흐르는 가장자리에 위치
        dfs(cxy_idx + 1, visited_list, core + 1, l_len)
        return

    # 4방향 확인
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
        temp_visited = []
        nx, ny = cx, cy

        if dx == 0 and dy == 0:  dfs(cxy_idx + 1, visited_list, core, l_len)  # 가지 안뻗고 바로 넘기기
        else:
            flag_b = 0
            while 1:
                nx += dx
                ny += dy
#                print(nx, ny)

                if nx < 0 or ny < 0 or nx >= n or ny >= n:break

                if (nx, ny) in visited_list:
                    flag_b = 1
                    break
                else:                    temp_visited.append((nx, ny))

            if flag_b == 0:
                dfs(cxy_idx + 1, visited_list + temp_visited, core + 1, l_len + len(temp_visited))
            else:continue

    return


T = int(input())
for tc in range(1, T+1):
    n = int(input())  # N*N 엑시노스
    maps = [list(map(int, input().split())) for _ in range(n)]

    visited, cxy = [], []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                cxy.append((i, j))
                visited.append((i, j))

    result = []
    dfs(0, visited, 0, 0)

    max_core = -float('inf')
    min_line = float('inf')
    for r in result:
        max_core = max(max_core, r[0])
    for r in result:
        if r[0] == max_core:
            min_line = min(min_line, r[1])

    print(f'#{tc} {min_line}')