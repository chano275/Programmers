# n = int(input())
# ori = list(map(int, input().split()))
#
# temp = []
# for i in range(len(ori)):
#     temp.append(max(ori[i] + (i+1), i+1))
#
# swap = []
# for i in range(len(ori)):
#     swap.append(temp[i] - ori[i])
#
# swap.sort(reverse=True)
#
# ans_temp = sum(ori)
#
# ans = 0
# if ans_temp >= 2 * n:
#     print(ans)
# else:
#     for elem in swap:
#         ans_temp += elem
#         ans += 1
#         if ans_temp >= 2 * n:
#             print(ans)
#             break
#####################################################################
# n = int(input())
# maps = [list(map(int, input().split())) for _ in range(n)]
# visited = [[float('inf')] * n for _ in range(n)]
# visited[0][0] = 0
#
# from collections import deque
#
#
# queue = deque()
# queue.append((0,0, 0))
#
# while queue:
#     cx, cy, cur_fuel = queue.popleft()
#     for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
#         nx, ny = cx+dx, cy+dy
#         if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
#
#         temp_fuel = 0
#         check = maps[cx][cy] - maps[nx][ny]
#         if check < 0: temp_fuel += 2 * abs(check)
#         elif check == 0:temp_fuel += 1
#
#         if visited[nx][ny] > cur_fuel + temp_fuel:
#             visited[nx][ny] = cur_fuel + temp_fuel
#             queue.append((nx, ny, cur_fuel + temp_fuel))
#
# print(visited[n-1][n-1])
#####################################################################
t = 10
for tc in range(1, t+1):
    v, e = map(int, input().split())
    ori_edges = list(map(int, input().split()))

    zin_ip = [0] * (v+1)
    graph = [[] for _ in range(v+1)]

    for i in range(e):
        front, rear = ori_edges[2 * i], ori_edges[2 * i + 1]
        zin_ip[rear] += 1
        graph[front].append(rear)

    from collections import deque


    queue = deque()
    visited = []
    for i in range(1, len(zin_ip)):
        if zin_ip[i] == 0:
            queue.append(i)
            visited.append(i)

    while queue:
        cur = queue.popleft()
        for elem in graph[cur]:
            zin_ip[elem] -= 1

        for i in range(1, len(zin_ip)):
            if zin_ip[i] == 0 and i not in visited:
                queue.append(i)
                visited.append(i)

    print(f'#{tc} ', end = '')
    for elem in visited:
        print(elem, end = ' ')

    print('')