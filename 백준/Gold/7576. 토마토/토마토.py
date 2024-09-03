"""
bfs 정석으로
start_point queue에 넣어서 먼저 주변 처리하는 식으로
"""
from collections import deque


def zero_checker(arr):
    zero_flag = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                zero_flag = 1

    if zero_flag == 0:        return False
    else: return True

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

if not zero_checker(maps):
    print(0)
else:
    ans = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                queue.append((i, j))

    while 1:
        temp_queue = deque()
        ans += 1
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == -1:continue
                    elif maps[nx][ny] == 0:
                        maps[nx][ny] = 1
                        temp_queue.append((nx, ny))  # 새로운 큐에 붙이고 dfs 느낌으로 해야할거같은데 / 할때마다 ans += 1 하고고

        # print(temp_queue)
        # for _m in maps:
        #     print(_m)

        queue = temp_queue

        if not queue:break

    if zero_checker(maps):print(-1)  # true : 0이 있다
    else:  print(ans - 1)