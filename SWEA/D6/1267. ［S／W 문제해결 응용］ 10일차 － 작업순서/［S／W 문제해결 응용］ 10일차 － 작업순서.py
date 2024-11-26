# n = int(input())
# ori = list(map(int, input().split()))

# sec = []
# for i in range(len(ori)):
#     sec.append(max(ori[i] + (i+1), i+1))

# plus = []
# for i in range(len(ori)):
#     plus.append(sec[i] - ori[i])

# plus.sort(reverse=True)
# print(plus)

# ans = 0
# temp = sum(ori)
# if temp >= 2 * n:
#     print(ans)
# else:
#     for elem in plus:
#         temp += elem
#         ans += 1

#         if temp >= 2 * n:
#             print(ans)
#             break


######################################################
# from collections import deque


# n = int(input())
# maps = [list(map(int, input().split())) for _ in range(n)]
# visited = [[float('inf')] * n for _ in range(n)]


# def bfs():
#     queue = deque()
#     queue.append((0,0, 0))
#     visited[0][0] = 0

#     while queue:
#         cx, cy, cur_fuel = queue.popleft()
#         for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
#             temp_fuel = 0
#             nx, ny = cx+dx, cy+dy
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:continue

#             difference = maps[cx][cy] - maps[nx][ny]

#             if difference < 0:temp_fuel = abs(difference) * 2
#             elif difference > 0: temp_fuel = 0
#             else: temp_fuel = 1

#             if visited[nx][ny] > cur_fuel + temp_fuel:
#                 visited[nx][ny] = cur_fuel + temp_fuel
#                 queue.append((nx, ny, cur_fuel + temp_fuel))

# bfs()

# print(visited[n-1][n-1])

################################################################

t = 10
for tc in range(1, t+1):
    v, e = map(int, input().split())
    maps = list(map(int, input().split()))

    zin_ip = [0] * (v+1)
    graph = [[] for _ in range(v+1)]

    for i in range(e):
        front = maps[2 * i] 
        rear  = maps[2 * i + 1]
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